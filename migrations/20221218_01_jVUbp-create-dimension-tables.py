"""
create dimension tables
"""

from yoyo import step

__depends__ = {"20221023_01_JVZ9p-create-bike_sharing-schema"}

steps = [
    step(
        """
        CREATE TABLE bike_sharing.d_stations (
            station_id          SMALLINT NOT NULL PRIMARY KEY,
            name                VARCHAR(50),
            address             VARCHAR(70),
            lat                 NUMERIC,
            lon                 NUMERIC,
            capacity            SMALLINT,
            datetime_inserted   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        "DROP TABLE bike_sharing.stations"
    ),
    step(
        """
        CREATE TABLE bike_sharing.d_date (
            date                     DATE NOT NULL PRIMARY KEY,
            epoch                    BIGINT NOT NULL,
            day_suffix               VARCHAR(4) NOT NULL,
            day_name                 VARCHAR(9) NOT NULL,
            day_of_week              INT NOT NULL,
            day_of_month             INT NOT NULL,
            day_of_quarter           INT NOT NULL,
            day_of_year              INT NOT NULL,
            week_of_month            INT NOT NULL,
            week_of_year             INT NOT NULL,
            week_of_year_iso         CHAR(10) NOT NULL,
            month_actual             INT NOT NULL,
            month_name               VARCHAR(9) NOT NULL,
            month_name_abbreviated   CHAR(3) NOT NULL,
            quarter_actual           INT NOT NULL,
            quarter_name             VARCHAR(9) NOT NULL,
            year_actual              INT NOT NULL,
            first_day_of_week        DATE NOT NULL,
            last_day_of_week         DATE NOT NULL,
            first_day_of_month       DATE NOT NULL,
            last_day_of_month        DATE NOT NULL,
            first_day_of_quarter     DATE NOT NULL,
            last_day_of_quarter      DATE NOT NULL,
            first_day_of_year        DATE NOT NULL,
            last_day_of_year         DATE NOT NULL,
            mmyyyy                   CHAR(6) NOT NULL,
            mmddyyyy                 CHAR(10) NOT NULL,
            weekend_indr             BOOLEAN NOT NULL
        )
        """,
        "DROP TABLE bike_sharing.d_date"
    )
]
