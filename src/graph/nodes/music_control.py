from src.graph.action_node import ActionNode, NodeIODataType


class MusicControlNode(ActionNode):
    create_queue = True

    input_data_type = {NodeIODataType.NONE, NodeIODataType.URL}
    output_data_type = {NodeIODataType.NONE}

    async def execute(self, input_data=None):
        self.data['video_url'] = input_data

        self.send_node_to_queue()

    def validate_inputs(self) -> bool:
        return True
