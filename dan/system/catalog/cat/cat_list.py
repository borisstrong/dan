import sys
sys.path.append('system/catalog/classes')
from classes.Catalog import Catalog


def cat_list(SITE):
    print('FUNCTION -> system_> calalog -> cat -> cat_list')

    CATALOG = Catalog(SITE)
    rows = CATALOG.getItems()
    print(rows)

    row_out = ''
    i = 1
    for row in rows:
        row_out += f''' <tr>
            <td>{ i }</td>
            <td>
                <div class="flex_row contextmenu_wrap">
                    <svg class="contextmenu_ico" title="Действия" data-id="{ row['id'] }">
                        <use xlink:href="/templates/system/svg/sprite.svg#menu_3"></use>
                    </svg>
                </div>
            </td>
            <td>
                <a href="/system/catalog/cat/{ row['id'] }">{ row['name'] }</a>
            </td>
        </tr>
        '''
        i += 1

    SITE.content += f'''<div class="bg_gray">
        <h1>Каталоги</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>Каталог</span>
        </div>
        <div class="flex_row_start">
            <a href="/system/catalog/cat/add" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#folder_add"></use></svg>
                <div class="ico_rectangle_text">Добавить каталог</div>
            </a>
            <a href="/system/catalod/item/add" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#paper_add"></use></svg>
                <div class="ico_rectangle_text">Добавить элемент</div>
            </a>
            <a href="/system/catalod/help" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#help"></use></svg>
                <div class="ico_rectangle_text">Помощь</div>
            </a>
        </div>
        <table class="admin_table even_odd">
            <tr>
                <th style="width:50px;">Id</th>
                <th style="width:50px;">&nbsp;</th>
                <th>Наменование</th>
            </tr>
            { row_out }
        </table>
    </div>
    '''
