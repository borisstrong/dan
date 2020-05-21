def catalog(SITE):
    print('FUNCTION -> calalog')
    print(SITE.p)
    SITE.content += """<div class="bg_gray">
        <h1>Каталог</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>Каталог</span>
        </div>
        <div class="flex_row_start">
            <a href="/system/catalod/section/add" target="blank" class="ico_rectangle_container">
                <svg><use xlink:href="/templates/system/svg/sprite.svg#folder_add"></use></svg>
                <div class="ico_rectangle_text">Добавить раздел</div>
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
            <tr>
                <td>1</td>
                <td>
                    <div class="flex_row contextmenu_wrap">
                        <svg class="contextmenu_ico" title="Действия" data-id="1">
                            <use xlink:href="/templates/system/svg/sprite.svg#menu_3"></use>
                        </svg>
                    </div>
                </td>
                <td>
                    <a href="/system/catalog/add/12">catalog</a>
                </td>
            </tr>
            <tr>
                <td>1</td>
                <td>
                    <div class="flex_row contextmenu_wrap">
                        <svg class="contextmenu_ico" title="Действия" data-id="1">
                            <use xlink:href="/templates/system/svg/sprite.svg#menu_3"></use>
                        </svg>
                    </div>
                </td>
                <td>
                    <a href="/system/catalog/add/12">catalog</a>
                </td>
            </tr>
        </table>
    </div>
    """
