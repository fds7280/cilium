# Copyright Authors of Cilium
# SPDX-License-Identifier: Apache-2.0

from scapy.all import *

from pkt_defs_common import *

ipv6_test_ext4_tcp_syn = (
    Ether(src=mac_one, dst=mac_two) /
    IPv6(src=v6_node_one, dst=v6_node_two, nh=60) /
    IPv6ExtHdrDestOpt(nh=60) /
    IPv6ExtHdrDestOpt(nh=60) /
    IPv6ExtHdrDestOpt(nh=60) /
    IPv6ExtHdrDestOpt(nh=6) /
    TCP(sport=tcp_src_one, dport=tcp_svc_one, flags="S")
)
