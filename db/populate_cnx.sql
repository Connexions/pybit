--
-- Data for Name: arch; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY arch (id, name) FROM stdin;
4	ipad
5	mobile
9	desktop
10	kindle
12	any
\.


--
-- Data for Name: buildclients; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY buildclients (id, name) FROM stdin;
1	arm01
2	arm02
3	buildbox
\.


--
-- Data for Name: distribution; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY distribution (id, name) FROM stdin;
2	cnx
3	ccap
4	openstax
\.


--
-- Data for Name: format; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY format (id, name) FROM stdin;
2	pdf
3	epub
4	mobi
5	completezip
\.


--
-- Data for Name: job; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY job (id, packageinstance_id, buildclient_id) FROM stdin;
1	6	\N
\.


--
-- Data for Name: jobstatus; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY jobstatus (id, job_id, status_id, "time") FROM stdin;
1	1	1	2012-11-29 16:03:28.78304
\.


--
-- Data for Name: package; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY package (id, version, name) FROM stdin;
3	23	collection2345
4	1.2	m9003
\.


--
-- Data for Name: packageinstance; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY packageinstance (id, package_id, arch_id, suite_id, dist_id, format_id, master) FROM stdin;
6	3	9	3	3	2	t
7	4	5	3	2	2	f
8	4	12	3	3	5	f
9	3	12	4	3	5	f
10	4	12	4	3	4	f
11	3	12	3	3	5	f
\.


--
-- Data for Name: status; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY status (id, name) FROM stdin;
1	Waiting
2	Blocked
3	Cancelled
4	Building
5	Failed
6	Uploaded
7	Done
\.


--
-- Data for Name: suite; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY suite (id, name) FROM stdin;
3	latex
4	princexml
\.


--
-- Data for Name: suitearches; Type: TABLE DATA; Schema: public; Owner: reedstrm
--

COPY suitearches (id, suite_id, arch_id) FROM stdin;
6	3	9
7	4	9
8	4	5
\.


