import json

from core.CoreConfig import CoreConfig

print(bool(CoreConfig.get_caps_by_type("android_kobiton").get("noReset")))