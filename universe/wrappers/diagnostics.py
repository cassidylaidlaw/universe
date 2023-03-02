import logging
import six
from universe import pyprofile, vectorized

logger = logging.getLogger(__name__)

# Not used in core; but used in play_flashgames
class Diagnostics(vectorized.Wrapper):

    def step(self, action_n):
        observation_n, reward_n, done_n, info = self.env.step(action_n)
        # We want this to be above Mask, so we know whether or not a
        # particular index is resetting.
        if self.unwrapped.diagnostics:
            with pyprofile.push('vnc_env.diagnostics.add_metadata'):
                self.unwrapped.diagnostics.add_metadata(observation_n, info['n'])
        return observation_n, reward_n, done_n, info
