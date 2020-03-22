insert into angajati values(1, 'Ionut', TO_DATE('10/7/1985','DD/MM/YYYY'), TO_DATE('12/12/2010','DD/MM/YYYY'));
insert into angajati values(2, 'Vasile', TO_DATE('04/03/1970','DD/MM/YYYY'), TO_DATE('07/09/2011','DD/MM/YYYY'));
insert into angajati values(3, 'Gigi', TO_DATE('02/01/1990','DD/MM/YYYY'), TO_DATE('14/11/2011','DD/MM/YYYY'));
insert into angajati values(4, 'Florin', TO_DATE('19/05/1991','DD/MM/YYYY'), TO_DATE('02/01/2012','DD/MM/YYYY'));
insert into angajati values(5, 'Alex', TO_DATE('28/04/1983','DD/MM/YYYY'), TO_DATE('21/03/2015','DD/MM/YYYY'));

insert into Marci_Masini values("brand_seq".NEXTVAL,'Ford');
insert into Marci_Masini values("brand_seq".NEXTVAL,'Audi');
insert into Marci_Masini values("brand_seq".NEXTVAL,'Skoda');
insert into Marci_Masini values("brand_seq".NEXTVAL,'BMW');
insert into Marci_Masini values("brand_seq".NEXTVAL,'Dacia');
insert into Marci_Masini values("brand_seq".NEXTVAL,'Toyota');

insert into Modele_Masini values("model_seq".NEXTVAL, 'Focus II 2005-2009 1.6 TDCI',1);
insert into Modele_Masini values("model_seq".NEXTVAL, 'Fabia 1999-2007 1.4 MPI',3);
insert into Modele_Masini values("model_seq".NEXTVAL, 'Seria 3 1999-2005 2.0D',4);
insert into Modele_Masini values("model_seq".NEXTVAL, 'A4 2003-2007 1.6 Benzina',2);
insert into Modele_Masini values("model_seq".NEXTVAL, 'Mondeo III 1999-2004 2.0 TDCI',1);
insert into Modele_Masini values("model_seq".NEXTVAL, 'Avensis 2010-2016 2.0 Diesel',6);
insert into Modele_Masini values("model_seq".NEXTVAL, 'Logan 2004-2008 1.6 16v',5);

insert into categorie values("category_seq".NEXTVAL, 'Sistem racire');
insert into categorie values("category_seq".NEXTVAL, 'Suspensii');
insert into categorie values("category_seq".NEXTVAL, 'Sistem franare');
insert into categorie values("category_seq".NEXTVAL, 'Filtre');
insert into categorie values("category_seq".NEXTVAL, 'Distributie');

insert into produse values("product_seq".NEXTVAL, 'Telescop fata', 250.0, 30, 2);
insert into produse values("product_seq".NEXTVAL, 'Filtru ulei MANN', 30.0, 50, 4);
insert into produse values("product_seq".NEXTVAL, 'Antigel', 10.0, 150, 1);
insert into produse values("product_seq".NEXTVAL, 'Disc frana fata Brembo', 100.0, 50, 3);
insert into produse values("product_seq".NEXTVAL, 'Disc frana spate Brembo', 75.0, 50, 3);
insert into produse values("product_seq".NEXTVAL, 'Telescop spate', 200.0, 30, 2);
insert into produse values("product_seq".NEXTVAL, 'Curea distributie', 70.0, 100, 5);
insert into produse values("product_seq".NEXTVAL, 'Filtru aer MANN', 25.0, 50, 4);
insert into produse values("product_seq".NEXTVAL, 'Lant distributie', 200.0, 40, 5);

insert into compatibilitati values(1,4);
insert into compatibilitati values(3,9);
insert into compatibilitati values(7,3);
insert into compatibilitati values(1,5);
insert into compatibilitati values(4,1);
insert into compatibilitati values(4,6);
insert into compatibilitati values(5,9);
insert into compatibilitati values(3,4);
insert into compatibilitati values(3,5);
insert into compatibilitati values(6,3);
insert into compatibilitati values(3,3);
insert into compatibilitati values(1,3);
insert into compatibilitati values(2,3);
insert into compatibilitati values(4,3);
insert into compatibilitati values(5,3);
insert into compatibilitati values(6,2);
insert into compatibilitati values(7,7);
insert into compatibilitati values(4,7);
insert into compatibilitati values(6,8);
insert into compatibilitati values(5,8);
insert into compatibilitati values(2,2);

commit;
