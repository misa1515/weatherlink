"""Constants for the Weatherlink integration."""
from enum import StrEnum

DOMAIN = "weatherlink"
VERSION = "0.9.4"

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
    HUM_IN = "hum_in"
    HUM_OUT = "hum_out"
    RAIN_DAY = "rain_day"
    RAIN_MONTH = "rain_month"
    RAIN_RATE = "rain_rate"
    RAIN_STORM = "rain_storm"
    RAIN_STORM_START = "rain_storm_start"
    RAIN_YEAR = "rain_year"
    SENSOR_TYPE = "sensor_type"
    SOLAR_PANEL_VOLT = "solar_panel_volt"
    SOLAR_RADIATION = "solar_radiation"
    SUPERCAP_VOLT = "supercap_volt"
    TEMP_IN = "temp_in"
    TEMP_OUT = "temp_out"
    THW_INDEX = "thw_index"
    THSW_INDEX = "thsw_index"
    TRANS_BATTERY_FLAG = "trans_battery_flag"
    TRANS_BATTERY_VOLT = "trans_battery_volt"
    UUID = "station_id_uuid"
    WET_BULB = "wet_bulb"
    WIND_CHILL = "wind_chill"
    WIND_DIR = "wind_dir"
    WIND_MPH = "wind_mph"
    WIND_GUST_MPH = "wind_gust_mph"
