class AliceAnswer:
    def __init__(self, q: "AliceQuestion"):
        self.data = {
            "response": {
                "text": "Простите, произошла непредвиденная ошибка!",
                "tts": "Простите, произошла непредвиденная ошибка!",
                "end_session": False
            },
            "session": {
                "session_id": q.session_id,
                "message_id": q.message_id,
                "user_id": q.user_id
            },
            "version": "1.0"
        }

    @property
    def text(self):
        return self.data['response']['text']

    @text.setter
    def text(self, txt):
        self.data['response']['text'] = txt.replace("+")
        self.data['response']['tts'] = txt


class AliceQuestion:
    def __init__(self, data):
        self.tz = data['meta']['timezone']
        self.command: str = data['request']['command']
        self.payload: dict = data['request'].get('payload', {})
        self.session_new = data['session']['new']
        self.session_id = data['session']["session_id"]
        self.message_id = data['session']["message_id"]
        self.user_id = data['session']["user_id"]

    def process(self):
        answer = AliceAnswer(self)
        if "эхо" in self.command:
            answer.text = self.command.replace("эхо", "отвечаю: - - -")
        else:
            answer.text = "Команда не найдена, попробуй ещё раз"

        return answer.data
