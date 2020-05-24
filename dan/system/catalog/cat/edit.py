def edit(SITE):
    print('FUNCTION -> system_> calalog -> cat -> edit')

    if SITE.p[2] == 'edit':
        title = 'Редактировать каталог'
        action = 'update'
        catalog = {'title': '', 'url': ''}
    else:
        title = 'Добавить  каталог'
        action = 'insert'
        catalog = {'title': '', 'url': ''}

    SITE.content += '''<div class="bg_gray">
        <h1>''' + title + '''</h1>
        <div class="breadcrumbs">
            <a href="/system/"><svg class="home"><use xlink:href="/templates/system/svg/sprite.svg#home"></use></svg></a> 
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <a href="/system/catalog">Каталог</a>
            <svg><use xlink:href="/templates/system/svg/sprite.svg#arrow_right_1"></use></svg>
            <span>''' + title + '''</span>
        </div>
		<form method="post" action="/system/catalog/cat/''' + action + '''">
			<div class="tc_container">
				<div class="flex_row p_5_20">
					<div class="tc_item_l">Наименование</div>
					<div class="tc_item_r flex_grow">
						<input class="input" name="name" placeholder="Интернет магазин" required value="''' + catalog['title'] + '''">
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l">URL адрес каталога</div>
					<div class="tc_item_r flex_grow">
						<input id="sef" class="input" name="sef" placeholder="catalog" required value="''' + catalog['url'] + '''">
						<div id="url_status"></div>
					</div>
				</div>
				<div class="flex_row p_5_20">
					<div class="tc_item_l"><input class="button_green" type="submit" name="submit" value="Сохранить"></div>
					<div class="tc_item_r flex_grow"><input class="button_white" type="submit" name="cancel" value="Отменить"></div>
				</div>
			</div>
		</form>
    </div>
    '''
