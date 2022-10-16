from fastapi import FastAPI
import HumanFriendlyTime
app = FastAPI()


@app.get("/")
def root(time: str = ""):
    obj = HumanFriendlyTime.HumanFriendlyTime()
    if time == "":
        return {"HumanFriendlyTimeText": obj.get_human_friendly_time_now()}
    else:
        try:
            return {"HumanFriendlyTimeText": obj.get_human_friendly_time_string(time)}
        except TypeError as e:
            return {"HumanFriendlyTimeText": str(e)}
        except ValueError as e:
            return {"HumanFriendlyTimeText": str(e)}
