import miio
from influx_line_protocol import Metric


class XiaomiAirPurifier:

    def get_metric(self, ip, token=None):
        if token is None:
            token = self.__discover_token(ip)
        data = miio.airpurifier.AirPurifier(ip, token).status()
        metric = Metric("xiaomi-air-purifier")

        metric.add_value("is_on", data.power == 'on')
        metric.add_value("child_lock", data.child_lock)
        metric.add_value("aqi", 0 if data.aqi is None else data.aqi)
        metric.add_value("filter_hours_used", 0 if data.filter_hours_used is None else data.filter_hours_used)
        metric.add_value("filter_life_remaining",
                         0 if data.filter_life_remaining is None else data.filter_life_remaining)
        metric.add_value("humidity", 0 if data.humidity is None else data.humidity)
        metric.add_value("illuminance", 0 if data.illuminance is None else data.illuminance)
        metric.add_value("motor1_speed", 0 if data.motor_speed is None else data.motor_speed)
        metric.add_value("motor2_speed", 0 if data.motor2_speed is None else data.motor2_speed)
        metric.add_value("purify_volume", 0 if data.purify_volume is None else data.purify_volume)
        metric.add_value("temperature", 0.0 if data.temperature is None else data.temperature)
        metric.add_value("use_time", 0 if data.use_time is None else data.use_time)

        return metric

    def __discover_token(self, ip):
        data = miio.device.Device.discover(ip)
        if data is None:
            raise Exception("Device not found, or token autodiscovery is not supported")

        return data.checksum.hex()
