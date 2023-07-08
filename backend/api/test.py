from mahjong.hand_calculating.scores import ScoresCalculator
from mahjong.hand_calculating.hand_config import HandConfig, HandConstants

config1 = HandConfig()

config2 = HandConfig()
config2.is_dealer = True

calc = ScoresCalculator()
print(calc.calculate_scores(3, 40, config1,False))
print(calc.calculate_scores(3, 40, config2,False))