% Parent relationships
parent(shamrao, sanjay).
parent(venubai, sanjay).
parent(sanjay, kunal).
parent(smita, kunal).

% Gender information
male(shamrao).
male(sanjay).
male(kunal).

female(venubai).
female(smita).

% Marriage relationship
wife(smita, sanjay).
husband(sanjay, smita).


% -------- RULES --------

% Father
father(X, Y) :-
    parent(X, Y),
    male(X).

% Mother
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Child
child(X, Y) :-
    parent(Y, X).

% Son
son(X, Y) :-
    child(X, Y),
    male(X).

% Daughter
daughter(X, Y) :-
    child(X, Y),
    female(X).

% Sibling
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Grandparent
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Grandfather
grandfather(X, Y) :-
    grandparent(X, Y),
    male(X).

% Grandmother
grandmother(X, Y) :-
    grandparent(X, Y),
    female(X).
