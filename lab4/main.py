from lab4 import builder, mode

driver_name = input("Введите название драйвера > ")
driver_builder = builder.SDFabric.get_sd_driver(driver_name)

our_list = mode.DLL()
our_list.add_node('Hi')
our_list.add_node('Hey')
print(our_list)

our_list.set_structure_driver(driver_builder.build())
our_list.save()