"""Constants for the Weatherlink integration."""
from enum import StrEnum

DOMAIN = "weatherlink"
VERSION = "2024.1.0b5"

MANUFACTURER = "Davis Instruments"
CONFIG_URL = "https://www.weatherlink.com/"

CONF_API_VERSION = "api_version"
CONF_API_KEY_V2 = "api_key_v2"
CONF_API_SECRET = "api_secret"
CONF_API_TOKEN = "apitoken"
CONF_STATION_ID = "station_id"


class ApiVersion(StrEnum):
    """Supported API versions."""

    API_V1 = "api_v1"
    API_V2 = "api_v2"


class DataKey(StrEnum):
    """Keys for normalized observation data."""

    BAR_SEA_LEVEL = "bar_sea_level"
    BAR_TREND = "bar_trend"
    DATA_STRUCTURE = "data_structure"
    DEWPOINT = "dewpoint"
    HEAT_INDEX = "heat_index"
    HUM_EXTRA_1 = "hum_extra_1"
    HUM_EXTRA_2 = "hum_extra_2"
    HUM_EXTRA_3 = "hum_extra_3"
    HUM_EXTRA_4 = "hum_extra_4"
    HUM_EXTRA_5 = "hum_extra_5"
    HUM_EXTRA_6 = "hum_extra_6"
    HUM_EXTRA_7 = "hum_extra_7"
    HUM_IN = "hum_in"
    HUM_OUT = "hum_out"
    MOIST_SOIL_1 = "moist_soil_1"
    MOIST_SOIL_2 = "moist_soil_2"
    MOIST_SOIL_3 = "moist_soil_3"
    MOIST_SOIL_4 = "moist_soil_4"
    RAIN_DAY = "rain_day"
    RAIN_MONTH = "rain_month"
    RAIN_RATE = "rain_rate"
    RAIN_STORM = "rain_storm"
    RAIN_STORM_LAST = "rain_storm_last"
    RAIN_STORM_LAST_END = "rain_storm_last_end"
    RAIN_STORM_LAST_START = "rain_storm_last_start"
    RAIN_STORM_START = "rain_storm_start"
    RAIN_YEAR = "rain_year"
    SENSOR_TYPE = "sensor_type"
    SOLAR_PANEL_VOLT = "solar_panel_volt"
    SOLAR_RADIATION = "solar_radiation"
    SUPERCAP_VOLT = "supercap_volt"
    TEMP_1 = "temp_1"
    TEMP_2 = "temp_2"
    TEMP_3 = "temp_3"
    TEMP_4 = "temp_4"
    TEMP_EXTRA_1 = "temp_extra_1"
    TEMP_EXTRA_2 = "temp_extra_2"
    TEMP_EXTRA_3 = "temp_extra_3"
    TEMP_EXTRA_4 = "temp_extra_4"
    TEMP_EXTRA_5 = "temp_extra_5"
    TEMP_EXTRA_6 = "temp_extra_6"
    TEMP_EXTRA_7 = "temp_extra_7"
    TEMP_SOIL_1 = "temp_soil_1"
    TEMP_SOIL_2 = "temp_soil_2"
    TEMP_SOIL_3 = "temp_soil_3"
    TEMP_SOIL_4 = "temp_soil_4"
    TEMP_IN = "temp_in"
    TEMP_OUT = "temp_out"
    TIMESTAMP = "timestamp"
    THW_INDEX = "thw_index"
    THSW_INDEX = "thsw_index"
    TRANS_BATTERY_FLAG = "trans_battery_flag"
    TRANS_BATTERY_VOLT = "trans_battery_volt"
    UUID = "station_id_uuid"
    UV_INDEX = "uv_index"
    WET_BULB = "wet_bulb"
    WET_LEAF_1 = "wet_leaf_1"
    WET_LEAF_2 = "wet_leaf_2"
    WET_LEAF_3 = "wet_leaf_3"
    WET_LEAF_4 = "wet_leaf_4"
    WIND_CHILL = "wind_chill"
    WIND_DIR = "wind_dir"
    WIND_MPH = "wind_mph"
    WIND_GUST_MPH = "wind_gust_mph"
