import pandas as pd
from app.crud import crud_employer, crud_import_shift_reference
from app.db.session import sync_session as SessionLocal
from app.models.shift import Shift
from sqlalchemy.orm import Session


def import_shift(file_path):
    # create a new session
    db: Session = SessionLocal()
    file_name = file_path.split('/')[-1]

    # Creates a new import reference
    import_reference = crud_import_shift_reference.create(db, obj_in={"file": file_name})

    try:
        # Load data
        data = pd.read_csv(file_path, delimiter=';')

        # Convert 'data_marcacao' to datetime format
        data['data_marcacao'] = pd.to_datetime(data['data_marcacao'], errors='coerce')

        # Convert 'hora_marcacao' to timedelta
        data['hora_marcacao'] = pd.to_timedelta(data['hora_marcacao'] + ':00')

        # Combine 'data_marcacao' and 'hora_marcacao' to get a datetime
        data['marcacao'] = data['data_marcacao'] + data['hora_marcacao']

        # Remove rows with invalid dates
        data = data.dropna(subset=['marcacao'])

        for matricula, group_data in data.groupby('matricula'):
            employer = crud_employer.get_by_identifier(db, identifier=matricula)
            if employer is None:
                employer = crud_employer.create(db, obj_in={"identifier": matricula})

            last_shift = None
            event_order = {
                0: "start_shift",  # "Entrada"
                1: "start_lunch",  # "Inicio Intervalo"
                2: "end_lunch",  # "Fim Intervalo"
                3: "end_shift",  # "Saida"
            }

            for date, group_date in group_data.groupby(group_data['marcacao'].dt.date):
                event_index = 0
                for index, row in group_date.sort_values(by='marcacao').iterrows():
                    if event_index % 4 == 0:
                        last_shift = Shift(employer_id=employer.identifier, import_shift_id=import_reference.id)
                        db.add(last_shift)

                    setattr(last_shift, event_order[event_index % 4], row['marcacao'])
                    event_index += 1
        db.commit()

    except Exception as e:
        print(e)
        db.rollback()
        crud_import_shift_reference.remove(db, id=import_reference.id)
    finally:
        # close the session
        db.close()
