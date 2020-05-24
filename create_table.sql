CREATE TABLE IF NOT EXISTS `component` (
`id` int(10) unsigned NOT NULL,
  `component` varchar(255) NOT NULL,
  `type` varchar(50) NOT NULL,
  `name` varchar(255) NOT NULL,
  `settings` text NOT NULL,
  `ordering` int NOT NULL
) AUTO_INCREMENT=1;

--
-- Индексы таблицы `components`
--
ALTER TABLE `component`
 ADD PRIMARY KEY (`id`), ADD KEY `type` (`type`);

--
-- AUTO_INCREMENT для таблицы `components`
--
ALTER TABLE `component`
MODIFY `id` int(10) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;