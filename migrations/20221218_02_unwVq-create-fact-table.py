"""
create fact table
"""

from yoyo import step

__depends__ = {'20221218_01_jVUbp-create-dimension-tables'}

steps = [
    step(
        """
        CREATE TABLE bike_sharing.f_availability (
            station_id          SMALLINT REFERENCES bike_sharing.d_stations,
            last_reported_date  DATE REFERENCES bike_sharing.d_date,
            inserted_date       DATE REFERENCES bike_sharing.d_date,
            inserted_timestamp  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_reported       TIMESTAMP NOT NULL,
            is_installed        BOOLEAN,
            is_renting          BOOLEAN,
            is_returning        BOOLEAN,
            num_bikes_available SMALLINT,
            num_docks_available SMALLINT,
            PRIMARY KEY (station_id, last_reported)
        )
        """,
        "DROP TABLE bike_sharing.f_availability"
    )
]
