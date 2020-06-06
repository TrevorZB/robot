from stash import Page

p = Page(0)

p.print_grid()

print('############################')

p.update_avail('Weapon')
p.store_item('Weapon')

p.print_grid()

print('############################')

p.update_avail('Ring')
p.store_item('Ring')

p.print_grid()

print('############################')

p.update_avail('Belt')
p.store_item('Belt')

p.print_grid()

print('############################')

p.update_avail('Helm')
p.store_item('Helm')

p.print_grid()

print('weapons: ', p.weapons)
print('rings: ', p.rings)
print('belts: ', p.belts)
print('helms: ', p.helms)
print('amulets: ', p.amulets)
