--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

-- Started on 2021-08-26 03:04:25

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 200 (class 1259 OID 16731)
-- Name: aluguel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aluguel (
    codigo integer NOT NULL,
    codigo_cliente integer NOT NULL,
    codigo_funcionario integer NOT NULL,
    tempo_aluguel character varying NOT NULL,
    preco numeric NOT NULL,
    data_aluguel date NOT NULL
);


ALTER TABLE public.aluguel OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16737)
-- Name: aluguel_livro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aluguel_livro (
    codigo_aluguel integer NOT NULL,
    codigo_livro integer NOT NULL
);


ALTER TABLE public.aluguel_livro OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16740)
-- Name: autor_livro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.autor_livro (
    codigo_livro integer NOT NULL,
    autor character varying NOT NULL
);


ALTER TABLE public.autor_livro OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16746)
-- Name: categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria (
    codigo integer NOT NULL,
    descricao character varying NOT NULL
);


ALTER TABLE public.categoria OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16752)
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    codigo integer NOT NULL,
    nome character varying NOT NULL,
    cpf bigint NOT NULL,
    endereco character varying NOT NULL
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16758)
-- Name: funcionario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.funcionario (
    codigo integer NOT NULL,
    nome character varying NOT NULL,
    cpf bigint NOT NULL,
    endereco character varying NOT NULL,
    salario numeric NOT NULL
);


ALTER TABLE public.funcionario OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16764)
-- Name: livro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livro (
    codigo integer NOT NULL,
    titulo character varying NOT NULL,
    ano integer NOT NULL,
    edicao integer NOT NULL,
    editora character varying NOT NULL,
    quant_paginas numeric NOT NULL
);


ALTER TABLE public.livro OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 16770)
-- Name: livro_categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livro_categoria (
    codigo_livro integer NOT NULL,
    codigo_categoria integer NOT NULL
);


ALTER TABLE public.livro_categoria OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 16773)
-- Name: telefone_cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.telefone_cliente (
    codigo_cliente integer NOT NULL,
    ddd integer NOT NULL,
    numero numeric NOT NULL
);


ALTER TABLE public.telefone_cliente OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16779)
-- Name: telefone_funcionario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.telefone_funcionario (
    codigo_funcionario integer NOT NULL,
    ddd integer NOT NULL,
    numero numeric NOT NULL
);


ALTER TABLE public.telefone_funcionario OWNER TO postgres;

--
-- TOC entry 3051 (class 0 OID 16731)
-- Dependencies: 200
-- Data for Name: aluguel; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.aluguel VALUES (1, 1, 3, '12 dias', 40, '2021-07-14');
INSERT INTO public.aluguel VALUES (2, 3, 1, '6 dias', 20, '2021-07-16');
INSERT INTO public.aluguel VALUES (3, 1, 3, '15 dias', 50, '2021-07-24');
INSERT INTO public.aluguel VALUES (4, 1, 2, '14 dias', 40, '2021-07-24');
INSERT INTO public.aluguel VALUES (5, 2, 1, '10 dias', 35, '2021-08-01');
INSERT INTO public.aluguel VALUES (6, 3, 3, '20 dias', 65, '2021-08-05');


--
-- TOC entry 3052 (class 0 OID 16737)
-- Dependencies: 201
-- Data for Name: aluguel_livro; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.aluguel_livro VALUES (1, 2);
INSERT INTO public.aluguel_livro VALUES (1, 5);
INSERT INTO public.aluguel_livro VALUES (2, 4);
INSERT INTO public.aluguel_livro VALUES (3, 1);
INSERT INTO public.aluguel_livro VALUES (3, 2);
INSERT INTO public.aluguel_livro VALUES (4, 6);
INSERT INTO public.aluguel_livro VALUES (5, 3);
INSERT INTO public.aluguel_livro VALUES (5, 6);
INSERT INTO public.aluguel_livro VALUES (6, 3);


--
-- TOC entry 3053 (class 0 OID 16740)
-- Dependencies: 202
-- Data for Name: autor_livro; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.autor_livro VALUES (1, 'J K Rowling');
INSERT INTO public.autor_livro VALUES (2, 'Aluísio Azevedo');
INSERT INTO public.autor_livro VALUES (3, 'James Stewart');
INSERT INTO public.autor_livro VALUES (4, 'Adriana Almeida');
INSERT INTO public.autor_livro VALUES (5, 'José de Alencar');
INSERT INTO public.autor_livro VALUES (6, 'C S Lewis');


--
-- TOC entry 3054 (class 0 OID 16746)
-- Dependencies: 203
-- Data for Name: categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.categoria VALUES (1, 'cientifico');
INSERT INTO public.categoria VALUES (3, 'literatura');
INSERT INTO public.categoria VALUES (2, 'fantasia');
INSERT INTO public.categoria VALUES (4, 'nacional');


--
-- TOC entry 3055 (class 0 OID 16752)
-- Dependencies: 204
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.cliente VALUES (1, 'Caio Brandao', 78915965485, 'Av Mister Hull, 12');
INSERT INTO public.cliente VALUES (2, 'Alice Fortes', 85245695148, 'Av A, 45');
INSERT INTO public.cliente VALUES (3, 'Arthur Anthunes', 74125896355, 'Av Tupi Guarani, 96');


--
-- TOC entry 3056 (class 0 OID 16758)
-- Dependencies: 205
-- Data for Name: funcionario; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.funcionario VALUES (1, 'Atyla Torres', 45685214796, 'Rua da Feira do Conjunto, 11', 2000);
INSERT INTO public.funcionario VALUES (2, 'Eduarda', 14835785254, 'Rua da Eduarda, 76', 2500);
INSERT INTO public.funcionario VALUES (3, 'Bruno Eskinazi', 75698488852, 'Rua Guarjaca, 126', 3000);


--
-- TOC entry 3057 (class 0 OID 16764)
-- Dependencies: 206
-- Data for Name: livro; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.livro VALUES (1, 'Harry Potter e o prisioneiro', 2010, 1, 'moderna', 456);
INSERT INTO public.livro VALUES (2, 'O cortiço', 2004, 3, 'cultura', 207);
INSERT INTO public.livro VALUES (3, 'Calculo Experimental', 1998, 7, 'premium', 207);
INSERT INTO public.livro VALUES (4, 'Quimica Organica', 2003, 4, 'moderna', 654);
INSERT INTO public.livro VALUES (5, 'Iracema', 2001, 1, 'cultura', 154);
INSERT INTO public.livro VALUES (6, 'As cronicas de Narnia', 2005, 2, 'moderna', 480);


--
-- TOC entry 3058 (class 0 OID 16770)
-- Dependencies: 207
-- Data for Name: livro_categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.livro_categoria VALUES (1, 2);
INSERT INTO public.livro_categoria VALUES (2, 3);
INSERT INTO public.livro_categoria VALUES (3, 1);
INSERT INTO public.livro_categoria VALUES (4, 1);
INSERT INTO public.livro_categoria VALUES (5, 3);
INSERT INTO public.livro_categoria VALUES (6, 2);
INSERT INTO public.livro_categoria VALUES (2, 4);
INSERT INTO public.livro_categoria VALUES (5, 4);


--
-- TOC entry 3059 (class 0 OID 16773)
-- Dependencies: 208
-- Data for Name: telefone_cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.telefone_cliente VALUES (1, 81, 988243585);
INSERT INTO public.telefone_cliente VALUES (1, 85, 987849564);
INSERT INTO public.telefone_cliente VALUES (2, 85, 985749621);
INSERT INTO public.telefone_cliente VALUES (3, 84, 965874521);
INSERT INTO public.telefone_cliente VALUES (3, 81, 985489536);


--
-- TOC entry 3060 (class 0 OID 16779)
-- Dependencies: 209
-- Data for Name: telefone_funcionario; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.telefone_funcionario VALUES (1, 84, 988255584);
INSERT INTO public.telefone_funcionario VALUES (2, 11, 987841168);
INSERT INTO public.telefone_funcionario VALUES (2, 85, 985746928);
INSERT INTO public.telefone_funcionario VALUES (2, 97, 965874698);
INSERT INTO public.telefone_funcionario VALUES (3, 85, 985446936);


--
-- TOC entry 2895 (class 2606 OID 16786)
-- Name: aluguel_livro aluguel_livro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluguel_livro
    ADD CONSTRAINT aluguel_livro_pkey PRIMARY KEY (codigo_aluguel, codigo_livro);


--
-- TOC entry 2893 (class 2606 OID 16788)
-- Name: aluguel aluguel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluguel
    ADD CONSTRAINT aluguel_pkey PRIMARY KEY (codigo);


--
-- TOC entry 2897 (class 2606 OID 16790)
-- Name: autor_livro autor_livro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.autor_livro
    ADD CONSTRAINT autor_livro_pkey PRIMARY KEY (codigo_livro, autor);


--
-- TOC entry 2899 (class 2606 OID 16792)
-- Name: categoria categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_pkey PRIMARY KEY (codigo);


--
-- TOC entry 2901 (class 2606 OID 16794)
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (codigo);


--
-- TOC entry 2903 (class 2606 OID 16796)
-- Name: funcionario funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (codigo);


--
-- TOC entry 2907 (class 2606 OID 16798)
-- Name: livro_categoria livro_categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_categoria
    ADD CONSTRAINT livro_categoria_pkey PRIMARY KEY (codigo_livro, codigo_categoria);


--
-- TOC entry 2905 (class 2606 OID 16800)
-- Name: livro livro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro
    ADD CONSTRAINT livro_pkey PRIMARY KEY (codigo);


--
-- TOC entry 2909 (class 2606 OID 16802)
-- Name: telefone_cliente telefone_cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.telefone_cliente
    ADD CONSTRAINT telefone_cliente_pkey PRIMARY KEY (codigo_cliente, ddd, numero);


--
-- TOC entry 2911 (class 2606 OID 16804)
-- Name: telefone_funcionario telefone_funcionario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.telefone_funcionario
    ADD CONSTRAINT telefone_funcionario_pkey PRIMARY KEY (ddd, numero, codigo_funcionario);


--
-- TOC entry 2912 (class 2606 OID 24822)
-- Name: aluguel aluguel_codigo_cliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluguel
    ADD CONSTRAINT aluguel_codigo_cliente_fkey FOREIGN KEY (codigo_cliente) REFERENCES public.cliente(codigo) ON UPDATE CASCADE ON DELETE SET NULL NOT VALID;


--
-- TOC entry 2913 (class 2606 OID 24827)
-- Name: aluguel aluguel_codigo_funcionario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluguel
    ADD CONSTRAINT aluguel_codigo_funcionario_fkey FOREIGN KEY (codigo_funcionario) REFERENCES public.funcionario(codigo) ON UPDATE CASCADE ON DELETE SET NULL NOT VALID;


--
-- TOC entry 2914 (class 2606 OID 24787)
-- Name: aluguel_livro aluguel_livro_codigo_aluguel_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluguel_livro
    ADD CONSTRAINT aluguel_livro_codigo_aluguel_fkey FOREIGN KEY (codigo_aluguel) REFERENCES public.aluguel(codigo) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 2915 (class 2606 OID 24832)
-- Name: aluguel_livro aluguel_livro_codigo_livro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aluguel_livro
    ADD CONSTRAINT aluguel_livro_codigo_livro_fkey FOREIGN KEY (codigo_livro) REFERENCES public.livro(codigo) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;


--
-- TOC entry 2916 (class 2606 OID 24797)
-- Name: autor_livro autor_livro_codigo_livro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.autor_livro
    ADD CONSTRAINT autor_livro_codigo_livro_fkey FOREIGN KEY (codigo_livro) REFERENCES public.livro(codigo) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 2917 (class 2606 OID 24802)
-- Name: livro_categoria livro_categoria_codigo_categoria_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_categoria
    ADD CONSTRAINT livro_categoria_codigo_categoria_fkey FOREIGN KEY (codigo_categoria) REFERENCES public.categoria(codigo) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 2918 (class 2606 OID 24807)
-- Name: livro_categoria livro_categoria_codigo_livro_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_categoria
    ADD CONSTRAINT livro_categoria_codigo_livro_fkey FOREIGN KEY (codigo_livro) REFERENCES public.livro(codigo) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 2919 (class 2606 OID 24812)
-- Name: telefone_cliente telefone_cliente_codigo_cliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.telefone_cliente
    ADD CONSTRAINT telefone_cliente_codigo_cliente_fkey FOREIGN KEY (codigo_cliente) REFERENCES public.cliente(codigo) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


--
-- TOC entry 2920 (class 2606 OID 24817)
-- Name: telefone_funcionario telefone_funcionario_codigo_funcionario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.telefone_funcionario
    ADD CONSTRAINT telefone_funcionario_codigo_funcionario_fkey FOREIGN KEY (codigo_funcionario) REFERENCES public.funcionario(codigo) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;


-- Completed on 2021-08-26 03:04:25

--
-- PostgreSQL database dump complete
--

