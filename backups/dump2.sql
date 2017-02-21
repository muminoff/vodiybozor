--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.2
-- Dumped by pg_dump version 9.6.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: vodiybozor
--

COPY categories (id, name, created) FROM stdin;
1	Авто-улов	2017-02-15 02:21:41.739717+00
2	Кўчмас-мулк	2017-02-15 02:21:41.739717+00
3	Маиший техника	2017-02-15 02:21:41.739717+00
4	Уй-рўзғор буюмлари	2017-02-15 02:21:41.739717+00
5	Кийим-кечак	2017-02-15 02:21:41.739717+00
6	Спорт анжомлари	2017-02-15 02:21:41.739717+00
7	Телефон	2017-02-15 02:21:41.739717+00
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vodiybozor
--

COPY users (id, first_name, last_name, username, is_admin, is_active, joined) FROM stdin;
160546867	Qudratillo		PIRATEDRAKE	t	t	2017-02-10 23:03:16.317933+00
260951612	ВЭБозор	Админ	Vebozoradmin	t	f	2017-02-10 11:23:53.408407+00
167188863	(( Imrоnchik	))		f	t	2017-02-14 22:57:58.197157+00
256412	Иззатбек	Мусаев	andbozor	t	t	2017-02-10 21:41:41.684446+00
292814220	12 22			f	t	2017-02-14 23:04:15.323614+00
69508059	Шах ан Шах		Sefevie	f	f	2017-02-10 22:29:58.965547+00
882017	Jafar		jafarjon	f	t	2017-02-11 13:30:04.609239+00
167385938	Farangiz			f	t	2017-02-11 18:14:42.249224+00
1438222	10:11	ÏšŁøM ßęK TDŸÛÛ		f	t	2017-02-11 22:04:49.884794+00
226467064	Sanjeek	Scofield	SanjeekScofield	f	f	2017-02-12 01:05:35.458282+00
255710274	I	Muhammadali	Cordiodoctor	f	t	2017-02-10 09:41:28.867114+00
231826623	Алмаз	Муйдинов		f	t	2017-02-12 05:00:09.567127+00
113363905	Madinabonu	Agzamova		f	t	2017-02-12 06:31:28.56616+00
79861994	АБУ ХИКМАТ			f	t	2017-02-07 20:54:25.93352+00
8092351	Kozimjon		Kozimjon707	f	f	2017-02-07 20:59:13.903749+00
287724279	Jorabek	Yusupov	Jorabek_Yusupov	f	f	2017-02-12 21:09:11.959526+00
1738671	Андижанец		alibahodur	t	t	2017-02-07 13:40:07.663531+00
44133074	Djo	Black	anjanlik	t	t	2017-02-07 14:02:22.806306+00
132655850	Abror Akramovich			f	t	2017-02-10 22:42:10.341472+00
303204903	Izzatillo	OOO"BOZ FARM"	OOO_BOZ_FARM	f	t	2017-02-13 14:31:24.461096+00
38564275	Шухратбек		otajonov11	f	f	2017-02-10 12:39:14.98385+00
285376238	Marhabo			f	t	2017-02-10 18:26:39.106203+00
188212873	Ulugbek	Ulugbek		f	t	2017-02-13 18:17:57.482014+00
198735717	Бону			f	t	2017-02-13 17:41:22.197587+00
97130731	OYBEK			f	t	2017-02-13 20:19:44.241456+00
198576829	♡♥♡МММ♡♥♡			f	t	2017-02-13 20:45:04.652079+00
147067071	Abdujalil			f	t	2017-02-13 22:05:15.06992+00
308731616	23903			f	t	2017-02-14 09:17:32.200152+00
315858961	Qosimov			f	t	2017-02-14 11:21:52.475324+00
220891996	UzMaN		Anjansky	f	t	2017-02-14 20:20:26.129639+00
77348597	S.B.R			f	t	2017-02-15 08:35:26.042238+00
77765328	M.R		MpurposeR	f	t	2017-02-15 08:54:53.850062+00
332902324	+998977777777		SIDIQJONOV	f	t	2017-02-15 09:18:46.209162+00
209987951	PRINCE 707		Olganimda_izlama_yorim	f	t	2017-02-15 09:27:20.755437+00
325990467	To'lqin	Nuraddinov		f	t	2017-02-15 09:38:26.512008+00
173051862	Black	Star		f	t	2017-02-15 09:47:51.585907+00
88211257	Javlonbek		JavlonbekToshmatov	f	t	2017-02-15 10:17:53.492923+00
284153855	©®7			f	t	2017-02-15 10:29:02.647561+00
289865361	Anvar	Tuxtaev		f	t	2017-02-15 11:43:52.787708+00
282067233	Avulova	Dildora		f	t	2017-02-15 11:45:10.385495+00
174431626	Eldorbek	Abdurashidov	Eldorbek94	f	t	2017-02-15 11:52:30.297559+00
204507280	007		futbol90	f	t	2017-02-15 12:19:06.096626+00
284133535	Trap bassss			f	t	2017-02-15 13:05:18.390688+00
213632408	0708	.		f	t	2017-02-15 13:08:33.571061+00
130601559	RAXMATULLO			f	t	2017-02-09 20:44:35.40357+00
182691886	$Ibrokhim	Ergashev	Ibrokhim_06	f	t	2017-02-15 11:44:51.337064+00
137587999	TIMUR	Timur		f	t	2017-02-16 09:46:47.767654+00
126235361	M1O			f	t	2017-02-16 10:54:02.268356+00
137684218	Ислом	Ашурв		f	t	2017-02-16 15:32:38.929456+00
202970222	Smart	Boy	TraderAdmin	f	t	2017-02-15 08:49:15.121548+00
90276273	+998945677744		MrKhann	f	t	2017-02-18 20:09:50.509494+00
250826346	K		KoMa1222	f	t	2017-02-18 22:02:59.815151+00
376455305	...			f	t	2017-02-18 22:08:45.328039+00
163624943	Black ☆		Wetyu45	f	t	2017-02-18 22:10:24.707169+00
55160536	Dobriy sinko			f	t	2017-02-18 22:19:01.806851+00
201240386	Abdurazzoq	Xasanov		f	t	2017-02-18 22:26:56.641523+00
322854740	AZIZ		Muxsinjonov	f	t	2017-02-18 22:28:44.554406+00
183705829	Toxtasin	Raximov		f	t	2017-02-18 22:36:15.118845+00
2669804	Азизбек	Абдумаликов	Abdumalikoov	f	t	2017-02-18 22:39:31.341621+00
145237218	Халимжон	6767		f	t	2017-02-18 22:42:49.143058+00
24139624	+998977777577			f	t	2017-02-18 22:44:10.827526+00
2843309	Tog'enmanu	Tanimadimi		f	t	2017-02-18 22:54:02.162217+00
248665004	ÀŁÍ😉			f	t	2017-02-18 22:54:40.687951+00
223577213	БЕМ И ЖЕК	Bem & Jek		f	t	2017-02-18 23:01:27.142096+00
166264856	**8583__		uztelegramist	f	t	2017-02-18 23:02:21.262127+00
281169150	Олимов			f	t	2017-02-18 23:19:41.134557+00
200243917	Хамдам	Хаджиев		f	t	2017-02-18 23:43:16.552666+00
310426145	Muxammad	Rasul		f	t	2017-02-19 00:09:48.455073+00
233665340	Umarganov	_95		f	t	2017-02-19 00:32:55.239079+00
360703068	Abdug'affor	Sharipov		f	t	2017-02-19 01:51:26.962481+00
195257972	Muzaffar			f	t	2017-02-19 01:57:24.302074+00
46597370	Jaxongir		YJaxongir	f	t	2017-02-19 04:34:00.198606+00
164397833	Imomjon	Karimov		f	t	2017-02-19 05:27:18.432998+00
51198967	اسلام		islam_khudoyberdiyev	f	t	2017-02-19 06:48:22.607121+00
327915404	Рихсивой	С		f	t	2017-02-19 07:21:32.725513+00
335609184	Шарипов		Sharipov2801	f	t	2017-02-19 09:54:05.450984+00
233519215	Shahzod			f	t	2017-02-19 09:58:29.549857+00
187296723	SWAT			f	t	2017-02-19 10:15:37.545935+00
284093472	Dilmirod			f	t	2017-02-19 10:29:17.418241+00
219780807	Idieal	Rich		f	t	2017-02-19 11:47:46.632242+00
254264062	Sanjarbek			f	t	2017-02-19 12:57:14.101723+00
326534061	Alik	AlikoF		f	t	2017-02-19 16:55:33.661556+00
92165988	(🔚Abror_Bek🔜)		officaliiiiAbrorbek	f	t	2017-02-19 20:02:18.367608+00
308924645	Atlant			f	t	2017-02-19 21:25:24.666787+00
310088711	Uralov	Asliddin		f	t	2017-02-19 21:41:32.945581+00
286388221	Shaxzod			f	t	2017-02-18 21:59:52.652205+00
2902951	Azizbek♬	ZyzzBro	AloneRomeo	f	t	2017-02-20 00:51:28.773145+00
314484653	Mansurbek			f	t	2017-02-20 13:07:17.488636+00
223129594	Jas	Kas		f	t	2017-02-20 14:57:40.215787+00
56781796	Sardor		muminofff	f	t	2017-02-07 07:23:19.290876+00
133986686	Arslanov			f	t	2017-02-20 16:59:16.489665+00
113424505	Mister_	Sherzodbek		f	t	2017-02-20 23:39:26.854908+00
32732672	Tony P.		iTonyParker	f	t	2017-02-21 02:30:05.832383+00
94662845	《Islom 93》			f	t	2017-02-20 10:27:28.620392+00
155940520	Android			f	t	2017-02-20 12:32:40.387385+00
\.


--
-- Data for Name: ads; Type: TABLE DATA; Schema: public; Owner: vodiybozor
--

COPY ads (id, category_id, user_id, data, is_closed, is_published, created) FROM stdin;
\.


--
-- Name: ads_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vodiybozor
--

SELECT pg_catalog.setval('ads_id_seq', 1, false);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vodiybozor
--

SELECT pg_catalog.setval('categories_id_seq', 1, false);


--
-- Data for Name: contacts; Type: TABLE DATA; Schema: public; Owner: vodiybozor
--

COPY contacts (user_id, phone_number, created) FROM stdin;
163624943	998933963730	2017-02-18 22:11:28.473231+00
322854740	998917794455	2017-02-18 22:34:14.856721+00
281169150	998936497773	2017-02-18 23:20:20.197299+00
310426145	+905347139609	2017-02-19 00:12:15.046842+00
233665340	+79522035707	2017-02-19 00:34:19.84807+00
287724279	998901400075	2017-02-19 08:51:27.741157+00
310088711	998909890624	2017-02-19 21:42:15.484012+00
155940520	998911727221	2017-02-20 12:35:31.198354+00
314484653	998914763737	2017-02-20 13:25:27.482224+00
56781796	821035027155	2017-02-17 06:47:20.648317+00
\.


--
-- Data for Name: drafts; Type: TABLE DATA; Schema: public; Owner: vodiybozor
--

COPY drafts (category_id, user_id, data, created) FROM stdin;
1	56781796	{"name": "Lacetti", "year": "2015", "price": "7000", "status": "яхши", "contact": "+998931234567", "mileage": "35000"}	2017-02-20 08:02:42.61976+00
\.


--
-- Data for Name: subscribers; Type: TABLE DATA; Schema: public; Owner: vodiybozor
--

COPY subscribers (category_id, user_id, subscribed_at) FROM stdin;
\.


--
-- Data for Name: visitors; Type: TABLE DATA; Schema: public; Owner: vodiybozor
--

COPY visitors (id, "timestamp", user_id, message) FROM stdin;
2	2017-02-20 08:11:47.843166+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487560307, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "test sardordan", "message_id": 1203}
3	2017-02-20 08:30:55.889361+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487561455, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "qwe", "message_id": 1207}
4	2017-02-20 08:31:01.121219+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487561460, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "popopo", "message_id": 1209}
5	2017-02-20 08:35:56.202483+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487561756, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "test", "message_id": 1213}
6	2017-02-20 08:52:38.364484+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487562758, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "shunaqami", "message_id": 1235}
7	2017-02-20 08:52:47.014247+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487562766, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "😐", "message_id": 1237}
8	2017-02-20 08:58:00.224145+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487563080, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "🚪 Уй-рўзғор буюмлари", "message_id": 1245}
9	2017-02-20 10:15:57.355828+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487567757, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "😃", "message_id": 1271}
10	2017-02-20 11:51:21.650282+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487573481, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "https://telegram.me/VodiyBozorBot?start=vCH1vGWJxfSeofSAs0K5PA", "entities": [{"type": "url", "length": 62, "offset": 0}], "message_id": 1294}
11	2017-02-20 11:52:22.484889+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487573542, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "https://telegram.me/VodiyBozorBot?contact=vCH1vGWJxfSeofSAs0K5PA", "entities": [{"type": "url", "length": 64, "offset": 0}], "message_id": 1298}
12	2017-02-20 11:59:50.756399+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487573990, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "/contact_JpWZo8r", "entities": [{"type": "bot_command", "length": 16, "offset": 0}], "message_id": 1306}
13	2017-02-20 11:59:58.753671+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487573998, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "/contact:JpWZo8r", "entities": [{"type": "bot_command", "length": 8, "offset": 0}], "message_id": 1308}
14	2017-02-20 12:00:27.824667+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487574027, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "/contact:JpWZo8r", "entities": [{"type": "bot_command", "length": 8, "offset": 0}], "message_id": 1310}
15	2017-02-20 12:01:18.64331+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487574078, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "/contact/JpWZo8r", "message_id": 1312}
16	2017-02-20 12:01:25.679639+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487574085, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "/contact_JpWZo8r", "entities": [{"type": "bot_command", "length": 16, "offset": 0}], "message_id": 1314}
17	2017-02-20 12:33:43.521072+00	155940520	{"chat": {"id": 155940520, "type": "private", "first_name": "Android"}, "date": 1487576023, "from": {"id": 155940520, "first_name": "Android"}, "text": "Menga not4 gadjetini sotib olmoqchiman", "message_id": 1322}
18	2017-02-20 12:35:17.95631+00	155940520	{"chat": {"id": 155940520, "type": "private", "first_name": "Android"}, "date": 1487576117, "from": {"id": 155940520, "first_name": "Android"}, "text": "Yoqimli ishtaxa", "message_id": 1324}
19	2017-02-20 12:35:55.225768+00	155940520	{"chat": {"id": 155940520, "type": "private", "first_name": "Android"}, "date": 1487576155, "from": {"id": 155940520, "first_name": "Android"}, "text": "Ismim O'tkirbek", "message_id": 1328}
20	2017-02-20 13:23:28.45885+00	314484653	{"chat": {"id": 314484653, "type": "private", "first_name": "Mansurbek"}, "date": 1487579008, "from": {"id": 314484653, "first_name": "Mansurbek"}, "text": "📺 Маиший техника", "message_id": 1342}
21	2017-02-20 13:25:18.001368+00	314484653	{"chat": {"id": 314484653, "type": "private", "first_name": "Mansurbek"}, "date": 1487579117, "from": {"id": 314484653, "first_name": "Mansurbek"}, "text": "A", "message_id": 1348}
22	2017-02-20 13:26:10.904741+00	314484653	{"chat": {"id": 314484653, "type": "private", "first_name": "Mansurbek"}, "date": 1487579170, "from": {"id": 314484653, "first_name": "Mansurbek"}, "text": "Хизмат ва таклифлар", "message_id": 1356}
23	2017-02-20 13:26:37.581797+00	314484653	{"chat": {"id": 314484653, "type": "private", "first_name": "Mansurbek"}, "date": 1487579197, "from": {"id": 314484653, "first_name": "Mansurbek"}, "text": "📱 Телефон", "message_id": 1364}
24	2017-02-20 13:34:12.313894+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487579652, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "Олмоқчиман", "message_id": 1370}
25	2017-02-20 14:26:41.689502+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487582801, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "Хизмат ва таклифлар", "message_id": 1378}
26	2017-02-20 15:46:19.146584+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487587578, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "Хизмат ва таклифлар", "message_id": 1388}
27	2017-02-20 15:46:30.155565+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487587589, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "Ха", "message_id": 1390}
28	2017-02-20 15:57:12.855331+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487588232, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "Олмоқчиман", "message_id": 1398}
29	2017-02-20 17:23:39.238283+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487593419, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "po", "message_id": 1406}
30	2017-02-20 17:54:36.382549+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487595276, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "йкйцк", "message_id": 1408}
31	2017-02-20 18:29:26.909087+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487597366, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "qwe", "message_id": 1414}
32	2017-02-20 18:29:38.535324+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487597378, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "wqrqwr", "message_id": 1416}
33	2017-02-21 02:30:23.825909+00	32732672	{"chat": {"id": 32732672, "type": "private", "username": "iTonyParker", "first_name": "Tony P."}, "date": 1487626223, "from": {"id": 32732672, "username": "iTonyParker", "first_name": "Tony P."}, "text": "🏠 Кўчмас-мулк", "message_id": 1425}
34	2017-02-21 02:31:10.910815+00	32732672	{"chat": {"id": 32732672, "type": "private", "username": "iTonyParker", "first_name": "Tony P."}, "date": 1487626270, "from": {"id": 32732672, "username": "iTonyParker", "first_name": "Tony P."}, "text": "Обуналарни кўрмоқчиман", "message_id": 1433}
35	2017-02-21 03:38:38.046007+00	56781796	{"chat": {"id": 56781796, "type": "private", "username": "muminofff", "first_name": "Sardor"}, "date": 1487630317, "from": {"id": 56781796, "username": "muminofff", "first_name": "Sardor"}, "text": "Хайрли тонг", "message_id": 1435}
\.


--
-- Name: visitors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vodiybozor
--

SELECT pg_catalog.setval('visitors_id_seq', 35, true);


--
-- PostgreSQL database dump complete
--

