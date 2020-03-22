CREATE TABLE angajati (
    id_angajat      NUMBER(4) NOT NULL,
    nume            VARCHAR2(35),
    data_nastere    DATE,
    data_angajare   DATE
);

ALTER TABLE angajati ADD CONSTRAINT angajati_pk PRIMARY KEY ( id_angajat );
ALTER TABLE angajati ADD CONSTRAINT ang_chk_cons_dt_ang CHECK(data_angajare>data_nastere);

CREATE TABLE categorie (
    id_categorie   NUMBER(3) NOT NULL,
    denumire       VARCHAR2(35)
);

ALTER TABLE categorie ADD CONSTRAINT categorie_pk PRIMARY KEY ( id_categorie );

CREATE TABLE clienti (
    id_client   NUMBER(5) NOT NULL,
    nume        VARCHAR2(35),
    Telefon     VARCHAR2(10),
    Serie       VARCHAR2(2),
    Nr_Serie    VARCHAR2(6)
);

ALTER TABLE clienti ADD CONSTRAINT clienti_pk PRIMARY KEY ( id_client );

CREATE TABLE comenzi (
    id_comanda   NUMBER(6) NOT NULL,
    total        NUMBER(10, 2),
    id_angajat   NUMBER(4) NOT NULL,
    id_client    NUMBER(5) NOT NULL
);

ALTER TABLE comenzi ADD CONSTRAINT comenzi_pk PRIMARY KEY ( id_comanda );
ALTER TABLE comenzi ADD CONSTRAINT comenzi_total_chk CHECK(total>0);

CREATE TABLE compatibilitati (
    id_model    NUMBER(3) NOT NULL,
    id_produs   NUMBER(5) NOT NULL
);

ALTER TABLE compatibilitati ADD CONSTRAINT compatibilitati_pk PRIMARY KEY ( id_model,
                                                                            id_produs );

CREATE TABLE marci_masini (
    id_marca     NUMBER(3) NOT NULL,
    nume_marca   VARCHAR2(35)
);

ALTER TABLE marci_masini ADD CONSTRAINT marci_masini_pk PRIMARY KEY ( id_marca );

CREATE TABLE modele_masini (
    id_model     NUMBER(3) NOT NULL,
    nume_model   VARCHAR2(35),
    id_marca     NUMBER(3) NOT NULL
);

ALTER TABLE modele_masini ADD CONSTRAINT modele_masin_pk PRIMARY KEY ( id_model );

CREATE TABLE produse (
    id_produs      NUMBER(5) NOT NULL,
    denumire       VARCHAR2(35),
    pret           NUMBER(10, 2),
    stock          NUMBER(5),
    id_categorie   NUMBER(3) NOT NULL
);

ALTER TABLE produse ADD CONSTRAINT produse_pk PRIMARY KEY ( id_produs );
ALTER TABLE produse ADD CONSTRAINT produse_pret_chk CHECK(pret > 0);
ALTER TABLE produse ADD CONSTRAINT produse_stock_chk CHECK(stock >= 0);


CREATE TABLE produse_comenzi (
    id_comanda   NUMBER(6) NOT NULL,
    id_produs    NUMBER(5) NOT NULL,
    Cantitate	 NUMBER(6) NOT NULL
);

ALTER TABLE produse_comenzi ADD CONSTRAINT produse_comenzi_pk PRIMARY KEY ( id_comanda,
                                                                            id_produs );
ALTER TABLE produse_comenzi ADD CONSTRAINT produse_comenzi_cant_chk CHECK(Cantitate >0);

ALTER TABLE comenzi
    ADD CONSTRAINT "angajati-comenzi" FOREIGN KEY ( id_angajat )
        REFERENCES angajati ( id_angajat );

ALTER TABLE produse
    ADD CONSTRAINT "categorie-produse" FOREIGN KEY ( id_categorie )
        REFERENCES categorie ( id_categorie );

ALTER TABLE comenzi
    ADD CONSTRAINT "client-comanda" FOREIGN KEY ( id_client )
        REFERENCES clienti ( id_client );

ALTER TABLE compatibilitati
    ADD CONSTRAINT compat_modele_masini_fk FOREIGN KEY ( id_model )
        REFERENCES modele_masini ( id_model );

ALTER TABLE compatibilitati
    ADD CONSTRAINT compatibilitati_produse_fk FOREIGN KEY ( id_produs )
        REFERENCES produse ( id_produs );

ALTER TABLE modele_masini
    ADD CONSTRAINT "marca-model" FOREIGN KEY ( id_marca )
        REFERENCES marci_masini ( id_marca );

ALTER TABLE produse_comenzi
    ADD CONSTRAINT produse_comenzi_comenzi_fk FOREIGN KEY ( id_comanda )
        REFERENCES comenzi ( id_comanda );

ALTER TABLE produse_comenzi
    ADD CONSTRAINT produse_comenzi_produse_fk FOREIGN KEY ( id_produs )
        REFERENCES produse ( id_produs );


-- Auto increments:
CREATE SEQUENCE "category_seq" START WITH 1 INCREMENT by 1;
CREATE SEQUENCE "brand_seq" START WITH 1 INCREMENT by 1;
CREATE SEQUENCE "model_seq" START WITH 1 INCREMENT by 1;
CREATE SEQUENCE "product_seq" START WITH 1 INCREMENT by 1;
CREATE SEQUENCE "order_seq" START WITH 1 INCREMENT by 1;
CREATE SEQUENCE "order_product_seq" START WITH 1 INCREMENT by 1;
CREATE SEQUENCE "clients_seq" START WITH 1 INCREMENT by 1;

commit;
