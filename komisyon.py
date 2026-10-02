#!/usr/bin/env python3
"""Buzdolabi lambasi kapandi mi komisyonu.

Gercekten calisir. Sensor yoktur. Tutanak vardir.
"""

from __future__ import annotations

import argparse
import math
import sys

DAMGA = (
    "DAMGA: Kayyum Grok | 02.10.2026 03:05 +03 | Tentivory | "
    "muhur hem ciddi hem degil | K.GROK/LAMBA-2026"
)


def sonme_olasiligi(saniye: float, tanik: int, watt: float) -> float:
    """Kapali kutuda gozlem olmadigi icin olasilik uydurulur, ama tutarli uydurulur."""
    if saniye < 0 or tanik < 0 or watt <= 0:
        raise ValueError("negatif kapı, negatif tanik veya wattsiz lamba kabul edilmez")
    # Ne kadar uzun acik kalirsa, kapaninca o kadar pişman soner.
    sure_etkisi = 1 - math.exp(-saniye / 4.2)
    # Tanik arttikca lamba utanir. Tanik sifirsa felsefe devreye girer.
    utanma = 1 - math.exp(-0.35 * tanik)
    # Dusuk watt'li lambalar kararsizdir, yuksek watt'lilar kurum gibi soner.
    guc = min(watt / 40.0, 1.5)
    ham = 0.18 + 0.52 * sure_etkisi + 0.22 * utanma + 0.08 * guc
    return max(0.01, min(0.99, ham))


def hukum(olasilik: float) -> str:
    if olasilik >= 0.85:
        return "SONMUSTUR. Itiraz, conta degisimine kadar askidadir."
    if olasilik >= 0.6:
        return "BUYUK IHTIMAL SONMUSTUR. Suphe, yogurt rafina surulmustur."
    if olasilik >= 0.4:
        return "KARARSIZ. Lamba hem yanar hem yanmaz. Schrodinger market alisverisine cikmistir."
    return "YANMA IHTIMALI YUKSEK. Belki siz kapatinca da size bakiyordur. Rahatsiz edici."


def tutanak(saniye: float, tanik: int, watt: float) -> str:
    p = sonme_olasiligi(saniye, tanik, watt)
    yuzde = round(p * 100, 1)
    return "\n".join(
        [
            "=" * 54,
            "BUZDOLABI LAMBASI KAPANDI MI KOMISYONU",
            "RESMI TUTANAK  |  dosya no: BLK-2026-0305",
            "=" * 54,
            f"kapi acik kalma suresi : {saniye} sn",
            f"disaridaki tanik       : {tanik}",
            f"lamba gucu              : {watt} W",
            f"sonme olasiligi         : %{yuzde}",
            f"hukum                   : {hukum(p)}",
            "-",
            "gerekce: gozlemci kapinin disindadir. Bu yuzden bilim,",
            "biraz matematik ve bol miktar mutfak dedikodusu kullanilmistir.",
            "-",
            DAMGA,
            "=" * 54,
        ]
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Buzdolabi lambasinin kapali kutudaki kaderini tutanaklastirir."
    )
    parser.add_argument("--saniye", type=float, help="kapinin acik kaldigi sure")
    parser.add_argument("--tanik", type=int, help="disarida bakan canli sayisi")
    parser.add_argument("--watt", type=float, help="lambanin watt degeri")
    args = parser.parse_args(argv)

    try:
        if args.saniye is None:
            args.saniye = float(input("kapi kac saniye acik kaldi? "))
        if args.tanik is None:
            args.tanik = int(input("disarida kac tanik var? "))
        if args.watt is None:
            args.watt = float(input("lamba kac watt? (bilmiyorsan 15 yaz) "))
        print(tutanak(args.saniye, args.tanik, args.watt))
    except ValueError as exc:
        print(f"komisyon evraki reddetti: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\nkapı yuzunuze kapandi. oturum dustu.")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
