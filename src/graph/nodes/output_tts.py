import json
from src.graph.action_node import ActionNode
from src.third_party.streamlabs import StreamlabsTTS, StreamlabsVoice
from src.voice.personality import Personality
from src.third_party.streamelements import StreamElementsTTS


class OutputTTSNode(ActionNode):
    create_queue = True  # Initially will be used for the Discord bot
    needs_uuid = True

    async def execute(self, input_data=None):
        self.graph_processor.add_personality()
        text = self.data['text']

        if not text:
            raise Exception("No text provided to speak, retry.")

        tts_url = StreamElementsTTS(StreamlabsVoice.Justin).get_url(text)
        self.data['tts_url'] = tts_url

        self.send_node_to_queue()

    def validate_inputs(self) -> bool:
        """
        Validate that text was provided in the data field
        """
        if 'text' not in self.data:
            return False

        return True
