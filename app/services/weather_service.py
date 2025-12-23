import requests
import logging

logger = logging.getLogger(__name__)


def fetch_geo_location(
    config_geo_url: str,
    api_key: str,
    city_name: str,
    state_code: str,
    country_code: str,
    timeout
):
    logger.info("Fetching geo location data")

    limit = 5
    url = f"{config_geo_url}?q={city_name},{state_code},{country_code}&limit={limit}&appid={api_key}"

    logger.debug(
        "Geo location request prepared",
        extra={
            "city": city_name,
            "state": state_code,
            "country": country_code,
            "limit": limit,
            "timeout": timeout
        }
    )

    try:
        response = requests.get(url, timeout=timeout)

        logger.debug(
            "Geo location API response received",
            extra={"status_code": response.status_code}
        )

        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            logger.error("Geo location response is not JSON")
            return None

        data = response.json()
        logger.info("Geo location data fetched successfully")
        return data

    except requests.exceptions.JSONDecodeError:
        logger.error("Geo location response contains invalid JSON", exc_info=True)

    except requests.exceptions.RequestException:
        logger.error("Geo location request failed", exc_info=True)

    return None


def fetch_current_weather_data(
    config_weather_url: str,
    api_key: str,
    latitude: float,
    longitude: float,
    timeout
):
    logger.info("Fetching current weather data")

    url = f"{config_weather_url}?lat={latitude}&lon={longitude}&appid={api_key}"

    logger.debug(
        "Weather request prepared",
        extra={"latitude": latitude, "longitude": longitude}
    )

    try:
        response = requests.get(url, timeout=timeout)

        logger.debug(
            "Weather API response received",
            extra={"status_code": response.status_code}
        )

        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            logger.error("Weather response is not JSON")
            return None

        data = response.json()
        logger.info("Weather data fetched successfully")
        return data

    except requests.exceptions.JSONDecodeError:
        logger.error("Weather response contains invalid JSON", exc_info=True)

    except requests.exceptions.RequestException:
        logger.error("Weather request failed", exc_info=True)

    return None
