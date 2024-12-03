import CosPlayTele as ct
import MissKon as mk
import Tool as t

items = ct.getCosPlayTeleItems()

#items = mk.getMissKonItems()
t.generate_items_file("CosPlayTele.txt",items,True)
print(1)