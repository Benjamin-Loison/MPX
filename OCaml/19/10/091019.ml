type arbre = Vide | N of int * arbre * arbre;;

let rec inserer a x = match a with
| Vide -> N(x, Vide, Vide)
| N(e, g, d) when e > x -> N(e, inserer g x, d)
| N(e, g, d) when e < x -> N(e, g, inserer d x)
| N(e, g, d) -> a;;

let rec arbre_of_list l = match l with
| [] -> Vide
| t::q -> inserer (arbre_of_list q) t;;

let a = arbre_of_list [11; 32; 27; 18; 14; 30; 16; 25];;

(*
       25
    16    30
  14 18   27 32
11

/!\ /!\ /!\ /!\
!= types de parcours: COURS
/!\ /!\ /!\ /!\

profondeur:
25 16 14 11 18 30 27 32 (prefixe)
11 14 16 18 25 27 30 32 (infixe)

11 14 18 16 27 32 30 25 (postfixe)

largeur:
25 16 30 14 18 27 32 11

*)

(* yep but prefer next one *)
let rec parcours_prefixe a = match a with
| Vide -> []
| N(x, g, d) -> x::(parcours_prefixe g)@(parcours_prefixe d);;

parcours_prefixe a;;

(* teacher ok *)
let parcours_prefixe a =
	let rec aux a acc = match a with
	| Vide -> acc
	| N(x, g, d) -> x::(aux g (aux d acc))
	in aux a [];;

parcours_prefixe a;;

(* *)

let rec parcours_infixe a = match a with
| Vide -> []
| N(x, g, d) -> (parcours_infixe g)@[x]@(parcours_infixe d);;

parcours_infixe a;;

let parcours_infixe a =
	let rec aux a acc = match a with
	| Vide -> acc
	| N(x, g, d) -> aux g (x::(aux d acc))
	in aux a [];;

parcours_infixe a;;

(* *)

let rec parcours_postfixe a = match a with
| Vide -> []
| N(x, g, d) -> (parcours_postfixe g)@(parcours_postfixe d)@[x];;

parcours_postfixe a;;

let parcours_postfixe a =
	let rec aux a acc = match a with
	| Vide -> acc
	| N(x, g, d) -> aux g (aux d (x::acc))
	in aux a [];;

parcours_postfixe a;;

(* yep all above *)

(* *)

let rec parcours_largeur a = match a with
| Vide -> []
| N(x, N(xg, gg, dg), N(xd, gd, dd)) ->
	x::[xg]@[xd]@(parcours_largeur gg)@(parcours_largeur dg)@(parcours_largeur gd)@(parcours_largeur dd)
| N(x, g, d) -> [x];;

let parcours_largeur a =
	let rec aux a acc = match a with
	| Vide -> acc
	| 
	in aux a [];;

parcours_largeur a;;

(*

On tient à jour une file d'attente des abres à traiter.
Cette liste contient initialement l'arbre de départ.
Le travail est terminé lorsque la file est vide.
Tant que la file n'est pas vide, on considère la tête de la file.
- si c'est l'arbre Vide on continue avec l'élement suivant.
- si c'est un noeud,
	on traite le noeud et on ajoute les sous-arbres gauche et droit en fin de file. 

*)

(* Hoffman el classico 2015 *)

(* teacher *)
let largeur a =
	let rec aux l = match l with
	| [] -> ()
	| Vide::q -> aux q
	| N(x, g, d)::q -> print_int x; print_char ' '; aux (q@[g; d])
	in aux [a];;

largeur a;;

let rec cstr l0 l1 = match l0, l1 with
| [], [] -> Vide
| t0::q0, t1::q1 when t0 < t1 -> N(t1, cstr())
| t0::q0, t1::q1 when t0 > t1 -> N(t0, );;

(* algorithme qui ne fonctionne pas avec des doublons 

Algo "reconstruire"

Soit A un arbre binaire qcq p et i ses parcours préfixes et infices.
Si p = i = [] alors A = Vide
Si p = i = [x] alors A = N(x, V, V)
Sinon le premier élément x de p est la racine de A
Ensuite i = i1@[x]@i2
On décompose p = x::p1@p2
où p1 est de la même longueur que i1.
A = N(x, reconstruire p1 i1; reconstruire p2 i2)
A = N(x, a1, a2) avec ai l'arbre de parcours pi et ii

*)

type arbrek = Vide | N of int*int*arbrek*arbrek;;

let rec count a = match a with
| Vide -> 0
| N(n, t, g, d) -> 1 + t + count d;;

count a;;

let rec inserer a x = match a with
| Vide -> N(x, 0, Vide, Vide)
| N(e, t, g, d) when e > x -> N(e, t + 1, inserer g x, d)
| N(e, t, g, d) when e < x -> N(e, t, g, inserer d x)
| N(e, t, g, d) -> a;;

let rec arbrek_of_list l = match l with
| [] -> Vide
| t::q -> inserer (arbrek_of_list q) t;;

let a = arbrek_of_list [11; 32; 27; 18; 14; 30; 16; 25];;

(*
1     3
 2   2
  3 1

p = x G D
      <x >x
*)

let rec recherche a x = match a with
| Vide -> false
| N(e, t, g, d) -> x = e || recherche g x || recherche d x;;

recherche a 13;;
recherche a 11;;

(*
       25
    16    30
  14 18   27 32
11

*)

let rec ieme a i = match a with
| Vide -> failwith "doesn't exist"
| N(x, t, g, d) when i = t + 1 -> x
| N(x, t, g, d) when i <= t -> ieme g i
| N(x, t, g, d) -> ieme d (i - t - 1);;

(*                       *)
(* 1  2   3 4  5   6  7 8 *)
(* 11 14 16 18 25 27 30 32 *)

ieme a 1;;
ieme a 2;;
ieme a 3;;
ieme a 4;;
ieme a 5;;
ieme a 6;;
ieme a 7;;
ieme a 8;;

let rec rg a x = match a with
| Vide -> failwith "not found"
| N(e, t, g, d) when x = e -> t + 1
| N(e, t, g, d) when x > e -> t + 1 + (rg d x)
| N(e, t, g, d) -> rg g x;;

(* or written like this *)
let rec rg a x = match a with
| Vide -> failwith "non present"
| N(e, t, g, d) -> if x < e then rg g x else if x > e then t + 1 + (rg d x) else
	t + 1;;

rg a 0;;
rg a 11;;
rg a 14;;
rg a 16;;
rg a 18;;
rg a 25;;
rg a 27;;
rg a 30;;
rg a 32;;

let rec verif a = match a with
| Vide -> true
| N(e, t, g, d) ->  && verif g && verif d;;