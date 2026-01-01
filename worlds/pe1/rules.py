from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import PE1World




def set_all_rules(world: PE1World) -> None:

    set_all_entrance_rules(world)
    set_completion_condition(world)




def set_all_entrance_rules(world: PE1World) -> None:

    manhattan_to_ch_norq = world.get_entrance("World Map to CH:NoRq")
    manhattan_to_pd_norq = world.get_entrance("World Map to PD:NoRq")
    manhattan_to_cp_norq = world.get_entrance("World Map to CP:NoRq")
    manhattan_to_sh_norq = world.get_entrance("World Map to SH:NoRq")
    manhattan_to_hs_norq = world.get_entrance("World Map to HS:NoRq")
    manhattan_to_ct_norq_or_cmbt_gk = world.get_entrance("World Map to CT:NoRq|Cmbt+GK")
    manhattan_to_sw_cmbt_pk_or_gk = world.get_entrance("World Map to SW:Cmbt+PK|GK")
    manhattan_to_wh_norq = world.get_entrance("World Map to WH:NoRq")
    manhattan_to_mu_norq = world.get_entrance("World Map to MU:NoRq")
    manhattan_to_cb_k1 = world.get_entrance("World Map to CB:K1")

    ch_norq_to_ch_cmbt = world.get_entrance("CH:NoRq to CH:Cmbt")
    ch_cmbt_to_ch_cmbt_tk = world.get_entrance("CH:Cmbt to CH:Cmbt+TK")
    ch_cmbt_to_ch_cmbt_rk = world.get_entrance("CH:Cmbt to CH:Cmbt+RK")
    ch_cmbt_rk_to_ch_boss_rk = world.get_entrance("CH:Cmbt+RK to CH:Boss+RK")

    pd_norq_to_pd_lk = world.get_entrance("PD:NoRq to PD:LK")
    pd_norq_to_pd_sk = world.get_entrance("PD:NoRq to PD:SK")
    pd_norq_to_pd_sj = world.get_entrance("PD:NoRq to PD:SJ")
    pd_sj_to_pd_cmbt_sj = world.get_entrance("PD:SJ to PD:Cmbt+SJ")
    pd_cmbt_sj_to_pd_boss_sj = world.get_entrance("PD:Cmbt+SJ to PD:Boss+SJ")
    pd_boss_sj_to_pd_boss_sj_junk = world.get_entrance("PD:Boss+SJ to PD:Boss+SJ+Junk")
    pd_boss_sj_to_pd_boss_sj_12rt = world.get_entrance("PD:Boss+SJ to PD:Boss+SJ+12RT")
    pd_boss_sj_12rt_to_pd_boss_sj_14rt = world.get_entrance("PD:Boss+SJ+12RT to PD:Boss+SJ+14RT")

    cp_norq_to_cp_cmbt = world.get_entrance("CP:NoRq to CP:Cmbt")
    cp_cmbt_to_cp_cmbt_zk = world.get_entrance("CP:Cmbt to CP:Cmbt+ZK")
    cp_cmbt_zk_to_cp_boss_zk = world.get_entrance("CP:Cmbt+ZK to CP:Boss+ZK")

    sh_norq_to_sh_wm = world.get_entrance("SH:NoRq to SH:WM")

    hs_norq_to_hs_gc = world.get_entrance("HS:NoRq to HS:GC")
    hs_norq_to_hs_bc = world.get_entrance("HS:NoRq to HS:BC")
    hs_norq_to_hs_cmbt = world.get_entrance("HS:NoRq to HS:Cmbt")
    hs_cmbt_to_hs_cmbt_ak = world.get_entrance("HS:Cmbt to HS:Cmbt+AK")
    hs_gc_to_hs_cmbt_gc = world.get_entrance("HS:GC to HS:Cmbt+GC")
    hs_bc_to_hs_cmbt_bc = world.get_entrance("HS:BC to HS:Cmbt+BC")
    hs_cmbt_bc_to_hs_cmbt_bc_3f = world.get_entrance("HS+Cmbt+BC to HS:Cmbt+BC+3F")
    hs_cmbt_bc_3f_to_hs_boss_bc_3f_ek = world.get_entrance("HS:Cmbt+BC+3F to HS:Boss+BC+3F+EK")

    ct_norq_or_cmbt_gk_to_ct_cmbt_or_cmbt_gk = world.get_entrance("CT:NoRq|Cmbt+GK to CT:Cmbt|Cmbt+GK")
    ct_cmbt_or_cmbt_gk_to_ct_boss_or_boss_gk = world.get_entrance("CT:Cmbt|Cmbt+GK to CT:Boss|Boss+GK")
    ct_cmbt_or_cmbt_gk_to_ct_cmbt_or_gk = world.get_entrance("CT:Cmbt|Cmbt+GK to CT:Cmbt|GK")
    ct_cmbt_or_gk_to_sw_cmbt_pk_or_gk = world.get_entrance("CT:Cmbt|GK to SW:Cmbt+PK|GK")

    sw_cmbt_pk_or_gk_to_sw_cmbt_pk_or_cmbt_gk = world.get_entrance("SW:Cmbt+PK|GK to SW:Cmbt+PK|Cmbt+GK")
    sw_cmbt_pk_or_cmbt_gk_to_sw_boss_pk_or_boss_gk = world.get_entrance("SW:Cmbt+PK|Cmbt+GK to SW:Boss+PK|Boss+GK")

    wh_norq_to_wh_cmbt = world.get_entrance("WH:NoRq to WH:Cmbt")
    wh_cmbt_to_wh_cmbt_wk = world.get_entrance("WH:Cmbt to WH:Cmbt+WK")
    wh_cmbt_wk_to_wh_boss_wk = world.get_entrance("WH:Cmbt+WK to WH:Boss+WK")

    mu_norq_to_mu_cmbt = world.get_entrance("MU:NoRq to MU:Cmbt")
    mu_cmbt_to_mu_cmbt_kk = world.get_entrance("MU:Cmbt to MU:Cmbt+KK")
    mu_cmbt_kk_to_mu_boss_kk = world.get_entrance("MU:Cmbt+KK to MU:Boss+KK")
    mu_boss_kk_to_liberty = world.get_entrance("MU:Boss+KK to SL:Boss+3C")
    liberty_to_cruiser = world.get_entrance("SL:Boss+3C to CR:Boss+3C")

    cb_k1_to_cb_k2 = world.get_entrance("CB:K1 to CB:K2")
    cb_k2_to_cb_k3 = world.get_entrance("CB:K2 to CB:K3")
    cb_k3_to_cb_k4 = world.get_entrance("CB:K3 to CB:K4")
    cb_k4_to_cb_k5 = world.get_entrance("CB:K4 to CB:K5")
    cb_k5_to_cb_k6 = world.get_entrance("CB:K5 to CB:K6")
    cb_k6_to_cb_k7 = world.get_entrance("CB:K6 to CB:K7")
    cb_k7_to_cb_spire = world.get_entrance("CB:K7 to CB:Boss+3C")


    set_rule(manhattan_to_ch_norq, lambda state: state.has("Area: Carnegie Hall", world.player))
    set_rule(manhattan_to_pd_norq, lambda state: state.has("Area: N.Y.P.D. #17", world.player))
    set_rule(manhattan_to_cp_norq, lambda state: state.has("Area: Central Park", world.player))
    set_rule(manhattan_to_sh_norq, lambda state: state.has("Area: Soho", world.player))
    set_rule(manhattan_to_hs_norq, lambda state: state.has("Area: Hospital", world.player))
    set_rule(manhattan_to_ct_norq_or_cmbt_gk, lambda state: state.has("Area: Chinatown", world.player))
    set_rule(manhattan_to_sw_cmbt_pk_or_gk, lambda state: state.has_all(("Area: Subway", "Gate Key"), world.player))
    set_rule(manhattan_to_wh_norq, lambda state: state.has("Area: Warehouse", world.player))
    set_rule(manhattan_to_mu_norq, lambda state: state.has("Area: Museum", world.player))
    set_rule(manhattan_to_cb_k1, lambda state: state.has_all(("Area: Chrysler BLDG.", "Chrysler Key 1"), world.player))

    set_rule(ch_norq_to_ch_cmbt, lambda state: state.has("Junk", world.player))
    set_rule(ch_cmbt_to_ch_cmbt_tk, lambda state: state.has("Theater Key", world.player))
    set_rule(ch_cmbt_to_ch_cmbt_rk, lambda state: state.has("Rehearse Key", world.player))
    set_rule(ch_cmbt_rk_to_ch_boss_rk, lambda state: state.has("Junk", world.player))

    set_rule(pd_norq_to_pd_lk, lambda state: state.has("Locker Key", world.player))
    set_rule(pd_norq_to_pd_sk, lambda state: state.has("Storage Key", world.player))
    set_rule(pd_norq_to_pd_sj, lambda state: state.has("Super Junk", world.player))
    set_rule(pd_sj_to_pd_cmbt_sj, lambda state: state.has("Junk", world.player))
    set_rule(pd_cmbt_sj_to_pd_boss_sj, lambda state: state.has("Junk", world.player))
    set_rule(pd_boss_sj_to_pd_boss_sj_junk, lambda state: state.has("Junk", world.player))
    set_rule(pd_boss_sj_to_pd_boss_sj_12rt, lambda state: state.has("Junk", world.player))
    set_rule(pd_boss_sj_12rt_to_pd_boss_sj_14rt, lambda state: state.has("Junk", world.player))

    set_rule(cp_norq_to_cp_cmbt, lambda state: state.has("Junk", world.player))
    set_rule(cp_cmbt_to_cp_cmbt_zk, lambda state: state.has("Zoo Key", world.player))
    set_rule(cp_cmbt_zk_to_cp_boss_zk, lambda state: state.has("Junk", world.player))

    set_rule(sh_norq_to_sh_wm, lambda state: state.has("Weapon Memo", world.player))

    set_rule(hs_norq_to_hs_gc, lambda state: state.has("Green Cardkey", world.player))
    set_rule(hs_norq_to_hs_bc, lambda state: state.has("Blue Cardkey", world.player))
    set_rule(hs_norq_to_hs_cmbt, lambda state: state.has("Junk", world.player))
    set_rule(hs_cmbt_to_hs_cmbt_ak, lambda state: state.has("Autopsy Key", world.player))
    set_rule(hs_gc_to_hs_cmbt_gc, lambda state: state.has("Junk", world.player))
    set_rule(hs_bc_to_hs_cmbt_bc, lambda state: state.has("Junk", world.player))
    set_rule(hs_cmbt_bc_to_hs_cmbt_bc_3f, lambda state: state.has_all(("Fuse 1", "Fuse 2", "Fuse 3"), world.player))
    set_rule(hs_cmbt_bc_3f_to_hs_boss_bc_3f_ek, lambda state: state.has("Elevator Key", world.player))

    set_rule(ct_norq_or_cmbt_gk_to_ct_cmbt_or_cmbt_gk, lambda state: state.has("Junk", world.player))
    set_rule(ct_cmbt_or_cmbt_gk_to_ct_boss_or_boss_gk, lambda state: state.has("Junk", world.player))
    set_rule(ct_cmbt_or_cmbt_gk_to_ct_cmbt_or_gk, lambda state: state.has("Pump Key", world.player))
    set_rule(ct_cmbt_or_gk_to_sw_cmbt_pk_or_gk, lambda state: state.has_all(("Area: Chinatown", "Area: Subway"), world.player))

    set_rule(sw_cmbt_pk_or_gk_to_sw_cmbt_pk_or_cmbt_gk, lambda state: state.has("Junk", world.player))
    set_rule(sw_cmbt_pk_or_cmbt_gk_to_sw_boss_pk_or_boss_gk, lambda state: state.has("Junk", world.player))

    set_rule(wh_norq_to_wh_cmbt, lambda state: state.has("Junk", world.player))
    set_rule(wh_cmbt_to_wh_cmbt_wk, lambda state: state.has("Warehouse Key", world.player))
    set_rule(wh_cmbt_wk_to_wh_boss_wk, lambda state: state.has("Junk", world.player))

    set_rule(mu_norq_to_mu_cmbt, lambda state: state.has("Junk", world.player))
    set_rule(mu_cmbt_to_mu_cmbt_kk, lambda state: state.has("Klamp Key", world.player))
    set_rule(mu_cmbt_kk_to_mu_boss_kk, lambda state: state.has("Junk", world.player))
    set_rule(mu_boss_kk_to_liberty, lambda state: state.has_all(("Narita", "Mayoke", "Hamaya", "M8000"), world.player))
    set_rule(liberty_to_cruiser, lambda state: state.has("DNA Bullets", world.player))

    set_rule(cb_k1_to_cb_k2, lambda state: state.has_all(("Chrysler Key 2", "M8000"), world.player))
    set_rule(cb_k2_to_cb_k3, lambda state: state.has("Chrysler Key 3", world.player))
    set_rule(cb_k3_to_cb_k4, lambda state: state.has("Chrysler Key 4", world.player))
    set_rule(cb_k4_to_cb_k5, lambda state: state.has("Chrysler Key 5", world.player))
    set_rule(cb_k5_to_cb_k6, lambda state: state.has("Chrysler Key 6", world.player))
    set_rule(cb_k6_to_cb_k7, lambda state: state.has("Chrysler Key 7", world.player))
    set_rule(cb_k7_to_cb_spire, lambda state: state.has_all(("Narita", "Mayoke", "Hamaya", "MP5A5"), world.player))

def set_completion_condition(world: PE1World) -> None:

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)