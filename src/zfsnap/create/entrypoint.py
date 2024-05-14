from __future__ import annotations
from argparse import Namespace
from typing import Optional, cast
import random

from ..zfs import LocalZfsCli
from ..constants import TAGS_PROPERTY
from .arguments import Args


def entrypoint(raw_args: Namespace) -> None:
  args = cast(Args, raw_args)

  if not args.dataset:
    raise ValueError(f"No dataset provided")
  snapname: str = args.snapname or to_hex(random.getrandbits(64), 16)

  print(f'Creating snapshot of "{args.dataset}"')
  LocalZfsCli().create_snapshot(dataset=args.dataset, name=snapname, recursive=args.recursive, properties={
    TAGS_PROPERTY: ','.join(args.tag)
  })


def to_hex(num: int, digits: int) -> str:
  hex_str = hex(num)[2:]
  hex_str_padded = f'{hex_str:0>{digits}}'
  return hex_str_padded
