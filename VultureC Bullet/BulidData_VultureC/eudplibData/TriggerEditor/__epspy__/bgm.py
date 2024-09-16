## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *

def _IGVA(vList, exprListGen):
    def _():
        exprList = exprListGen()
        SetVariables(vList, exprList)
    EUDOnStart(_)

def _CGFW(exprf, retn):
    rets = [ExprProxy(None) for _ in range(retn)]
    def _():
        vals = exprf()
        for ret, val in zip(rets, vals):
            ret._value = val
    EUDOnStart(_)
    return rets

def _ARR(items):
    k = EUDArray(len(items))
    for i, item in enumerate(items):
        k[i] = item
    return k

def _VARR(items):
    k = EUDVArray(len(items))()
    for i, item in enumerate(items):
        k[i] = item
    return k

def _SRET(v, klist):
    return List2Assignable([v[k] for k in klist])

def _SV(dL, sL):
    [d << s for d, s in zip(FlattenList(dL), FlattenList(sL))]

class _ATTW:
    def __init__(self, obj, attrName):
        self.obj = obj
        self.attrName = attrName

    def __lshift__(self, r):
        setattr(self.obj, self.attrName, r)

    def __iadd__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov + v)

    def __isub__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov - v)

    def __imul__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov * v)

    def __ifloordiv__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov // v)

    def __iand__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov & v)

    def __ior__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov | v)

    def __ixor__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov ^ v)

class _ARRW:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index

    def __lshift__(self, r):
        self.obj[self.index] = r

    def __iadd__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov + v

    def __isub__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov - v

    def __imul__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov * v

    def __ifloordiv__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov // v

    def __iand__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov & v

    def __ior__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov | v

    def __ixor__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov ^ v

def _L2V(l):
    ret = EUDVariable()
    if EUDIf()(l):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret

def _MVAR(vs):
    return List2Assignable([
        v.makeL() if IsEUDVariable(v) else EUDVariable() << v
        for v in FlattenList(vs)])

def _LSH(l, r):
    if IsEUDVariable(l):  return f_bitlshift(l, r)
    else: return l << r

## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY

# (Line 1) const bgm_switch = PVariable(); // 플레이어 bgm on/off 스위치
bgm_switch = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 2) const bgm_length = PVariable(); // 플레이어 bgm 길이
bgm_length = _CGFW(lambda: [PVariable()], 1)[0]
# (Line 4) function play_init() {
@EUDFunc
def f_play_init():
    # (Line 5) foreach (cp : EUDLoopPlayer()) {
    for cp in EUDLoopPlayer():
        # (Line 6) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 7) bgm_switch[cp] = 1;
        _ARRW(bgm_switch, cp) << (1)
        # (Line 8) }
        # (Line 9) }

    # (Line 11) function set_switch(cp, number) {

@EUDFunc
def f_set_switch(cp, number):
    # (Line 12) bgm_switch[cp] = number;
    _ARRW(bgm_switch, cp) << (number)
    # (Line 13) }
    # (Line 15) function set_length(cp, number) {

@EUDFunc
def f_set_length(cp, number):
    # (Line 16) bgm_length[cp] = number;
    _ARRW(bgm_length, cp) << (number)
    # (Line 17) }
    # (Line 19) function current_switch(cp) {

@EUDFunc
def f_current_switch(cp):
    # (Line 20) return bgm_switch[cp];
    EUDReturn(bgm_switch[cp])
    # (Line 21) }
    # (Line 23) function play() {

@EUDFunc
def f_play():
    # (Line 24) foreach (cp : EUDLoopPlayer()) {
    for cp in EUDLoopPlayer():
        # (Line 25) setcurpl(cp);
        f_setcurpl(cp)
        # (Line 26) bgm_length[cp]++;
        _ARRW(bgm_length, cp).__iadd__(1)
        # (Line 27) if (bgm_length[cp] == 1 && bgm_switch[cp] == 1) {
        if EUDIf()(EUDSCAnd()(bgm_length[cp] == 1)(bgm_switch[cp] == 1)()):
            # (Line 28) PlayWAV("staredit\\wav\\plutover.ogg");
            # (Line 29) }
            DoActions(PlayWAV("staredit\\wav\\plutover.ogg"))
            # (Line 30) if(bgm_length[cp] == 13620) {
        EUDEndIf()
        if EUDIf()(bgm_length[cp] == 13620):
            # (Line 31) bgm_length[cp] = 0;
            _ARRW(bgm_length, cp) << (0)
            # (Line 32) }
            # (Line 33) }
        EUDEndIf()
        # (Line 34) }