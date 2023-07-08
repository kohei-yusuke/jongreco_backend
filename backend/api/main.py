#ファイル名はmain.pyにする
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#POSTのためのモジュール
from pydantic import BaseModel

#mahjongライブラリ
#計算機
from mahjong.hand_calculating.scores import ScoresCalculator
from mahjong.hand_calculating.hand import HandCalculator
#牌
from mahjong.tile import TilesConverter
#役,オプションルール
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
#鳴き
from mahjong.meld import Meld
#風
from mahjong.constants import EAST, SOUTH, WEST, NORTH


app = FastAPI()

#通信するアプリのURLを記載する。デプロイしたとき注意
origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def Hello():
    return {"Hello":"World!"}

class HanFu(BaseModel):
    han: int
    hu: int
    is_chitoitsu: bool

@app.get("/score_calc/han/{han}/hu/{hu}/is_chitoitsu/{is_chitoitsu}")
def HanFuCalc(han: int,hu: int, is_chitoitsu: bool):
    if is_chitoitsu == True:
        hu = 25

    config1 = HandConfig()

    config2 = HandConfig()
    config2.is_tsumo = True

    calc = ScoresCalculator()
    ron_score_child=calc.calculate_scores(han,hu, config1,False)
    tsumo_score_child=calc.calculate_scores(han,hu, config2,False)
    
    config1.is_dealer = True
    config2.is_dealer = True

    ron_score_dealer=calc.calculate_scores(han,hu, config1,False)
    tsumo_score_dealer=calc.calculate_scores(han,hu, config2,False)
    return {"han":han,
            "hu": hu,
            "tsumo_child":tsumo_score_child, 
            "ron_child":ron_score_child,
            "tsumo_dealer": tsumo_score_dealer,
            "ron_dealer": ron_score_dealer
            }