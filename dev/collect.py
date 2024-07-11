def collect_device_methods():
    methods = """
get_number_of_chips_in_cluster
get_all_chips_in_cluster
set_driver_host_address_params
set_driver_eth_interface_params
set_device_l1_address_params
set_device_dram_address_params
using_harvested_soc_descriptors
get_harvesting_masks_for_soc_descriptors
noc_translation_en
get_virtual_soc_descriptors
get_clocks
get_target_mmio_device_ids
start_device
close_device
dram_membar
l1_membar
deassert_risc_reset
wait_for_non_mmio_flush
write_to_device
broadcast_write_to_cluster
write_to_device
rolled_write_to_device
read_from_device
write_to_sysmem
read_from_sysmem
channel_0_address
host_dma_address
translate_to_noc_table_coords
get_ethernet_fw_version
get_cluster_description
get_clocks
get_pcie_speed
read_from_device
write_to_device
get_target_mmio_device_ids
bar_read32
bar_write32
read_from_sysmem
get_harvested_coord_translation_map
"""
    unique_methods = sorted(set(methods.splitlines()))
    with open("result.txt", mode="wt") as f:
        for m in unique_methods:
            f.write(f"{m}\n")


collect_device_methods()
