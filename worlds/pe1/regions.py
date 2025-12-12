from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region
if TYPE_CHECKING:
    from .world import PE1World




def create_and_connect_regions(world: PE1World) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: PE1World) -> None:

    manhattan = Region("Manhattan (World Map)", world.player, world.multiworld)

    ch_norq = Region("Carnegie Hall: NoRq", world.player, world.multiworld)
    ch_cmbt = Region("Carnegie Hall: Cmbt", world.player, world.multiworld)
    ch_cmbt_tk = Region("Carnegie Hall: Cmbt+TK", world.player, world.multiworld)
    ch_cmbt_rk = Region("Carnegie Hall: Cmbt+RK", world.player, world.multiworld)
    ch_boss_rk = Region("Carnegie Hall: Boss+RK", world.player, world.multiworld)

    pd_norq = Region("N.Y.P.D. #17: NoRq", world.player, world.multiworld)
    pd_lk = Region("N.Y.P.D. #17: LK", world.player, world.multiworld)
    pd_sk = Region("N.Y.P.D. #17: SK", world.player, world.multiworld)
    pd_sj = Region("N.Y.P.D. #17: SJ", world.player, world.multiworld)
    pd_cmbt_sj = Region("N.Y.P.D. #17: Cmbt+SJ", world.player, world.multiworld)
    pd_boss_sj = Region("N.Y.P.D. #17: Boss+SJ", world.player, world.multiworld)
    pd_boss_sj_junk = Region("N.Y.P.D. #17: Boss+SJ+Junk", world.player, world.multiworld)
    pd_boss_sj_12rt = Region("N.Y.P.D. #17: Boss+SJ+12RT", world.player, world.multiworld)
    pd_boss_sj_14rt = Region("N.Y.P.D. #17: Boss+SJ+14RT", world.player, world.multiworld)

    cp_norq = Region("Central Park: NoRq", world.player, world.multiworld)
    cp_cmbt = Region("Central Park: Cmbt", world.player, world.multiworld)
    cp_cmbt_zk = Region("Central Park: Cmbt+ZK", world.player, world.multiworld)
    cp_boss_zk = Region("Central Park: Boss+ZK", world.player, world.multiworld)

    sh_norq = Region("Soho: NoRq", world.player, world.multiworld)
    sh_wm = Region("Soho: WM", world.player, world.multiworld)

    hs_norq = Region("Hospital: NoRq", world.player, world.multiworld)
    hs_gc = Region("Hospital: GC", world.player, world.multiworld)
    hs_bc = Region("Hospital: BC", world.player, world.multiworld)
    hs_cmbt = Region("Hospital: Cmbt", world.player, world.multiworld)
    hs_cmbt_gc = Region("Hospital: Cmbt+GC", world.player, world.multiworld)
    hs_cmbt_ak = Region("Hospital: Cmbt+AK", world.player, world.multiworld)
    hs_cmbt_bc = Region("Hospital: Cmbt+BC", world.player, world.multiworld)
    hs_cmbt_bc_3f = Region("Hospital: Cmbt+BC+3F", world.player, world.multiworld)
    hs_boss_bc_3f_ek = Region("Hospital: Boss+BC+3F+EK", world.player, world.multiworld)

    ct_norq_or_cmbt_gk = Region("Chinatown: NoRq|Cmbt+GK", world.player, world.multiworld)
    ct_cmbt_or_cmbt_gk = Region("Chinatown: Cmbt|Cmbt+GK", world.player, world.multiworld)
    ct_boss_or_boss_gk = Region("Chinatown: Boss|Boss+GK", world.player, world.multiworld)
    ct_cmbt_or_gk = Region("Chinatown: Cmbt|GK", world.player, world.multiworld)

    sw_cmbt_pk_or_gk = Region("Subway: Cmbt+PK|GK", world.player, world.multiworld)
    sw_cmbt_pk_or_cmbt_gk = Region("Subway: Cmbt+PK|Cmbt+GK", world.player, world.multiworld)
    sw_boss_pk_or_boss_gk = Region("Subway: Boss+PK|Boss+GK", world.player, world.multiworld)

    wh_norq = Region("Warehouse: NoRq", world.player, world.multiworld)
    wh_cmbt = Region("Warehouse: Cmbt", world.player, world.multiworld)
    wh_cmbt_wk = Region("Warehouse: Cmbt+WK", world.player, world.multiworld)
    wh_boss_wk = Region("Warehouse: Boss+WK", world.player, world.multiworld)

    mu_norq = Region("Museum: NoRq", world.player, world.multiworld)
    mu_cmbt = Region("Museum: Cmbt", world.player, world.multiworld)
    mu_cmbt_kk = Region("Museum: Cmbt+KK", world.player, world.multiworld)
    mu_boss_kk = Region("Museum: Boss+KK", world.player, world.multiworld)

    liberty = Region("Statue of Liberty: Boss", world.player, world.multiworld)
    cruiser = Region("Cruiser: Boss", world.player, world.multiworld)

    cb_k1 = Region("Chrysler BLDG.: Key 1", world.player, world.multiworld)
    cb_k2 = Region("Chrysler BLDG.: Key 2", world.player, world.multiworld)
    cb_k3 = Region("Chrysler BLDG.: Key 3", world.player, world.multiworld)
    cb_k4 = Region("Chrysler BLDG.: Key 4", world.player, world.multiworld)
    cb_k5 = Region("Chrysler BLDG.: Key 5", world.player, world.multiworld)
    cb_k6 = Region("Chrysler BLDG.: Key 6", world.player, world.multiworld)
    cb_k7 = Region("Chrysler BLDG.: Key 7", world.player, world.multiworld)
    cb_spire = Region("Chrysler BLDG.: Spire", world.player, world.multiworld)


    regions = [
              manhattan,
              ch_norq, ch_cmbt, ch_cmbt_tk, ch_cmbt_rk, ch_boss_rk,
              pd_norq, pd_lk, pd_sk, pd_sj, pd_cmbt_sj, pd_boss_sj, pd_boss_sj_junk, pd_boss_sj_12rt, pd_boss_sj_14rt,
              cp_norq, cp_cmbt, cp_cmbt_zk, cp_boss_zk,
              sh_norq, sh_wm,
              hs_norq, hs_gc, hs_bc, hs_cmbt,hs_cmbt_gc, hs_cmbt_ak, hs_cmbt_bc, hs_cmbt_bc_3f, hs_boss_bc_3f_ek,
              ct_norq_or_cmbt_gk, ct_cmbt_or_cmbt_gk, ct_boss_or_boss_gk, ct_cmbt_or_gk,
              sw_cmbt_pk_or_gk, sw_cmbt_pk_or_cmbt_gk, sw_boss_pk_or_boss_gk,
              wh_norq, wh_cmbt, wh_cmbt_wk, wh_boss_wk,
              mu_norq, mu_cmbt, mu_cmbt_kk, mu_boss_kk,
              liberty, cruiser,
              cb_k1, cb_k2, cb_k3, cb_k4, cb_k5, cb_k6, cb_k7, cb_spire
              ]

    world.multiworld.regions += regions


def connect_regions(world: PE1World) -> None:

    manhattan = world.get_region("Manhattan (World Map)")

    ch_norq = world.get_region("Carnegie Hall: NoRq")
    ch_cmbt = world.get_region("Carnegie Hall: Cmbt")
    ch_cmbt_tk = world.get_region("Carnegie Hall: Cmbt+TK")
    ch_cmbt_rk = world.get_region("Carnegie Hall: Cmbt+RK")
    ch_boss_rk = world.get_region("Carnegie Hall: Boss+RK")

    pd_norq = world.get_region("N.Y.P.D. #17: NoRq")
    pd_lk = world.get_region("N.Y.P.D. #17: LK")
    pd_sk = world.get_region("N.Y.P.D. #17: SK")
    pd_sj = world.get_region("N.Y.P.D. #17: SJ")
    pd_cmbt_sj = world.get_region("N.Y.P.D. #17: Cmbt+SJ")
    pd_boss_sj = world.get_region("N.Y.P.D. #17: Boss+SJ")
    pd_boss_sj_junk = world.get_region("N.Y.P.D. #17: Boss+SJ+Junk")
    pd_boss_sj_12rt = world.get_region("N.Y.P.D. #17: Boss+SJ+12RT")
    pd_boss_sj_14rt = world.get_region("N.Y.P.D. #17: Boss+SJ+14RT")

    cp_norq = world.get_region("Central Park: NoRq")
    cp_cmbt = world.get_region("Central Park: Cmbt")
    cp_cmbt_zk = world.get_region("Central Park: Cmbt+ZK")
    cp_boss_zk = world.get_region("Central Park: Boss+ZK")

    sh_norq = world.get_region("Soho: NoRq")
    sh_wm = world.get_region("Soho: WM")

    hs_norq = world.get_region("Hospital: NoRq")
    hs_gc = world.get_region("Hospital: GC")
    hs_bc = world.get_region("Hospital: BC")
    hs_cmbt = world.get_region("Hospital: Cmbt")
    hs_cmbt_gc = world.get_region("Hospital: Cmbt+GC")
    hs_cmbt_ak = world.get_region("Hospital: Cmbt+AK")
    hs_cmbt_bc = world.get_region("Hospital: Cmbt+BC")
    hs_cmbt_bc_3f = world.get_region("Hospital: Cmbt+BC+3F")
    hs_boss_bc_3f_ek = world.get_region("Hospital: Boss+BC+3F+EK")

    ct_norq_or_cmbt_gk = world.get_region("Chinatown: NoRq|Cmbt+GK")
    ct_cmbt_or_cmbt_gk = world.get_region("Chinatown: Cmbt|Cmbt+GK")
    ct_boss_or_boss_gk = world.get_region("Chinatown: Boss|Boss+GK")
    ct_cmbt_or_gk = world.get_region("Chinatown: Cmbt|GK")

    sw_cmbt_pk_or_gk = world.get_region("Subway: Cmbt+PK|GK")
    sw_cmbt_pk_or_cmbt_gk = world.get_region("Subway: Cmbt+PK|Cmbt+GK")
    sw_boss_pk_or_boss_gk = world.get_region("Subway: Boss+PK|Boss+GK")

    wh_norq = world.get_region("Warehouse: NoRq")
    wh_cmbt = world.get_region("Warehouse: Cmbt")
    wh_cmbt_wk = world.get_region("Warehouse: Cmbt+WK")
    wh_boss_wk = world.get_region("Warehouse: Boss+WK")

    mu_norq = world.get_region("Museum: NoRq")
    mu_cmbt = world.get_region("Museum: Cmbt")
    mu_cmbt_kk = world.get_region("Museum: Cmbt+KK")
    mu_boss_kk = world.get_region("Museum: Boss+KK")

    liberty = world.get_region("Statue of Liberty: Boss")
    cruiser = world.get_region("Cruiser: Boss")

    cb_k1 = world.get_region("Chrysler BLDG.: Key 1")
    cb_k2 = world.get_region("Chrysler BLDG.: Key 2")
    cb_k3 = world.get_region("Chrysler BLDG.: Key 3")
    cb_k4 = world.get_region("Chrysler BLDG.: Key 4")
    cb_k5 = world.get_region("Chrysler BLDG.: Key 5")
    cb_k6 = world.get_region("Chrysler BLDG.: Key 6")
    cb_k7 = world.get_region("Chrysler BLDG.: Key 7")
    cb_spire = world.get_region("Chrysler BLDG.: Spire")

# Bypassing region connection names for now to see if they'll work without them. That's a lot of connections to name...
    manhattan.connect(ch_norq)
    manhattan.connect(pd_norq)
    manhattan.connect(cp_norq)
    manhattan.connect(sh_norq)
    manhattan.connect(hs_norq)
    manhattan.connect(ct_norq_or_cmbt_gk)
    manhattan.connect(sw_cmbt_pk_or_gk)
    manhattan.connect(wh_norq)
    manhattan.connect(mu_norq)
    manhattan.connect(cb_k1)

    ch_norq.connect(ch_cmbt)
    ch_cmbt.connect(ch_cmbt_tk)
    ch_cmbt.connect(ch_cmbt_rk)
    ch_cmbt_rk.connect(ch_boss_rk)

    pd_norq.connect(pd_lk)
    pd_norq.connect(pd_sk)
    pd_norq.connect(pd_sj)
    pd_sj.connect(pd_cmbt_sj)
    pd_cmbt_sj.connect(pd_boss_sj)
    pd_boss_sj.connect(pd_boss_sj_junk)
    pd_boss_sj.connect(pd_boss_sj_12rt)
    pd_boss_sj_12rt.connect(pd_boss_sj_14rt)

    cp_norq.connect(cp_cmbt)
    cp_cmbt.connect(cp_cmbt_zk)
    cp_cmbt_zk.connect(cp_boss_zk)

    sh_norq.connect(sh_wm)

    hs_norq.connect(hs_gc)
    hs_norq.connect(hs_bc)
    hs_norq.connect(hs_cmbt)
    hs_cmbt.connect(hs_cmbt_ak)
    hs_gc.connect(hs_cmbt_gc)
    hs_bc.connect(hs_cmbt_bc)
    hs_cmbt_bc.connect(hs_cmbt_bc_3f)
    hs_cmbt_bc_3f.connect(hs_boss_bc_3f_ek)

    ct_norq_or_cmbt_gk.connect(ct_cmbt_or_cmbt_gk)
    ct_cmbt_or_cmbt_gk.connect(ct_boss_or_boss_gk)
    ct_cmbt_or_cmbt_gk.connect(ct_cmbt_or_gk)
    ct_cmbt_or_gk.connect(sw_cmbt_pk_or_gk)

    sw_cmbt_pk_or_gk.connect(sw_cmbt_pk_or_cmbt_gk)
    sw_cmbt_pk_or_cmbt_gk.connect(sw_boss_pk_or_boss_gk)

    wh_norq.connect(wh_cmbt)
    wh_cmbt.connect(wh_cmbt_wk)
    wh_cmbt_wk.connect(wh_boss_wk)

    mu_norq.connect(mu_cmbt)
    mu_cmbt.connect(mu_cmbt_kk)
    mu_cmbt_kk.connect(mu_boss_kk)
    mu_boss_kk.connect(liberty)
    liberty.connect(cruiser)

    cb_k1.connect(cb_k2)
    cb_k2.connect(cb_k3)
    cb_k3.connect(cb_k4)
    cb_k4.connect(cb_k5)
    cb_k5.connect(cb_k6)
    cb_k6.connect(cb_k7)
    cb_k7.connect(cb_spire)