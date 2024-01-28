import os
import random
from pexels_api import API as PexelsAPI
from src.graph.action_node import ActionNode

PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')


class PexelsSearchNode(ActionNode):
    create_queue = False

    async def execute(self, input_data=None):
        client = PexelsAPI(PEXELS_API_KEY)

        shuffle = self.data.get('shuffle', False)
        query = self.data['query']

        if not query:
            raise Exception("No Pexels search query provided")

        limit = 1
        if shuffle:
            limit = 10

        client.search(
            query=query,
            results_per_page=limit
        )

        results = client.get_entries()
        if not results:
            raise Exception("No results found for Pexels search query")

        if shuffle:
            random.shuffle(results)

        return results[0].original

    def validate_inputs(self) -> bool:
        """
        Validate that value was provided in the data field
        """
        if 'value' not in self.data:
            return False

        return True