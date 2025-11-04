from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)

FLY_SPEED_KMPH = 60.0  # 새 비행 속도 (km/h)
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)