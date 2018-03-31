class PortocolTest(pd_base_tests.ThriftInterfaceDataPlane):
	def __init__(self):
		pd_base_tests.ThriftInterfaceDataPlane.__init__(self, ["p4hdp"])

	def runTest(self):
		print
		sess_hdl = self.conn_mgr.client_init()

		dev_tgt = DevTarget_t(0, hex_to_i16(0xFFFF))
		device = 0

	
		# p4hdp_carrier_port_ecmp_group_setup(self.client, sess_hdl, dev_tgt)


		# protocol_identify_setup(self.client, sess_hdl, dev_tgt)
		# p4hdp_inner_ports_setup(self.client, sess_hdl, dev_tgt)
		# carrier_ports_vlan_map_entry_setup(self.client, sess_hdl, dev_tgt)
		# inner_vlan_port_map_entry_setup(self.client, sess_hdl, dev_tgt)



		# client_init(self.client, sess_hdl, dev_tgt)

		# #Add the default entries
		# populate_default_entries(self.client, sess_hdl, dev_tgt, ipv6_enabled,
		#                          acl_enabled, tunnel_enabled, multicast_enabled,
		#                          int_enabled)
		# ret_init = populate_init_entries(
		#     self.client, sess_hdl, dev_tgt, rewrite_index, rmac,
		#     inner_rmac_group, outer_rmac_group, ipv6_enabled, tunnel_enabled)

		# mdp_virtual_test_intf_config(self.client, sess_hdl, dev_tgt)

		# mdp_virtual_test_user_config(self.client, sess_hdl, dev_tgt)

		# mdp_virtual_test_arp_config(self.client, sess_hdl, dev_tgt)
		# #mdp_virtual_test_user_print()
		#mdp_virtual_test_route_config(self.client, sess_hdl, dev_tgt)


		self.conn_mgr.complete_operations(sess_hdl)


		# carrier_client_port = 1
		# carrier_network_port = 2

		# carrier_client_port_vlan = 10
		# carrier_network_port_vlan = 20

		# inner_protocol_port = 4


		# print "Checking load-balancing between 2 members"
		# npkts = 4
		# counts = [0, 0]
		# for i in xrange(npkts):
		#     ip_dst = "192.168.0.{}".format(i)
		#     pkt = simple_tcp_packet(pktlen=124, eth_dst='00:33:33:33:33:33', ip_dst=ip_dst, tcp_dport=117)
		#     exp_pkt1 = simple_tcp_packet(pktlen=128,  eth_dst='00:33:33:33:33:33', dl_vlan_enable=True, vlan_vid=200, ip_dst=ip_dst, tcp_dport=117)

		#     send_packet(self, carrier_network_port, str(pkt))
		#     eg_idx = verify_packet_any_port(self, exp_pkt1,  [7, 8])
		#     counts[eg_idx[0]] += 1
		# #self.assertTrue(counts[0] >= npkts / 4)
		# #self.assertTrue(counts[1] >= npkts / 4)
		# print "Checking load-balancing between 2 members: ", counts[0], counts[1],
		# #self.assertTrue(counts[0] + counts[1] == npkts)

		# print "Checking inner tcp bgp protocol pkt"
		# pkt1 = simple_tcp_packet(tcp_dport=179)        
		# pkt = simple_gre_packet(
		#     pktlen=124,        
		#     eth_src='00:77:66:55:44:33',
		#     eth_dst='00:55:55:55:55:55',
		#     ip_id=0,
		#     ip_dst='10.200.1.3',
		#     ip_src='10.100.1.1',
		#     ip_ttl=64,
		#     inner_frame=pkt1['IP'])
		# exp_pkt = simple_gre_packet(
		#     pktlen=128,
		#     dl_vlan_enable=True,
		#     vlan_vid=100,
		#     eth_src='00:77:66:55:44:33',
		#     eth_dst='00:55:55:55:55:55',
		#     ip_id=0,
		#     ip_dst='10.200.1.3',
		#     ip_src='10.100.1.1',
		#     ip_ttl=64,
		#     inner_frame=pkt1['IP'])        
		# send_packet(self, carrier_client_port, str(pkt))
		# print "Expecting packet on port", inner_protocol_port
		# verify_packets(self, exp_pkt, [inner_protocol_port])


		# print "Checking upd_dhcp  protocol pkt"
		# pkt = simple_udp_packet(udp_dport=67)        
		# exp_pkt = simple_udp_packet(pktlen=104,
		#               dl_vlan_enable=True,
		#               vlan_vid=100, udp_dport=67)

		# send_packet(self, carrier_client_port, str(pkt))
		# print "Expecting packet on port", inner_protocol_port
		# verify_packets(self, exp_pkt, [inner_protocol_port])


		# print "Checking l2 arp protocol pkt"
		# pkt = simple_arp_packet(pktlen=100)         
		# exp_pkt = simple_arp_packet(pktlen=104, vlan_vid=200)

		# send_packet(self, 5, str(pkt))
		# #verify_packets(self, exp_pkt, [inner_protocol_port])


		# print "Sending packet port 4 -> port 3 "
		# # pkt = simple_tcp_packet(
		# #      eth_dst='02:01:00:00:06:0c',
		# #      eth_src='00:12:01:00:00:01',
		# #      ip_dst='2.2.2.22',
		# #      ip_src='15.0.0.2',
		# #      ip_id=101,
		# #      ip_ttl=64,
		# #      ip_ihl=5)

		pkt = simple_tcp_packet(
			 eth_dst='04:01:03:00:06:0B',
			 eth_src='00:11:01:00:00:01',
			 ip_dst='20.0.0.2',
			 ip_src='10.0.0.2',
			 ip_id=101,
			 ip_ttl=64,
			 ip_ihl=5)

   
		send_packet(self, 5, str(pkt))




		pppoePkt = simple_pppoe_packet(
					eth_dst='02:01:00:00:06:0c',
					eth_src='00:12:01:00:00:01',
					ip_dst='2.2.2.222',
					ip_src='15.0.0.2',
					pppoe_version=1,
					pppoe_type=1,
					pppoe_code=0,
					pppoe_session=1)
    

		send_packet(self, 3, str(pppoePkt))



		self.conn_mgr.complete_operations(sess_hdl)
		self.conn_mgr.client_cleanup(sess_hdl)
