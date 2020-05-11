(*

dijk g s
	d = tableau n
	d(i) = w(s, i)
	E = 0, 1, ..., n - 1 \ s = sommets à traiter
	tant que E != emptyset
		u <- u in E
		d(u) <- min {d(v), v in E}
		E <- E \ u
		pour v in voisin(u)
			d(v) <- min {d(v), d(u) + w(u, v)}

*)

type poids = Inf | P of int;;

type gp = poids array array;;

type graphe = int list array;;

let som p0 p1 = match p0, p1 with
| Inf, _ | _, Inf -> Inf
| P a, P b -> P (a + b);;

let mini p0 p1 = match p0, p1 with
| Inf, x -> x
| P a, Inf -> P a (* or P(a) *)
| P a, P b -> P (min a b);;

(* < *)
let inferieur p0 p1 = match p0, p1 with
| Inf, _ -> false
| _, Inf -> true
| P(a), P(b) -> a < b;;

(*

nope

let recherche_min d e =
	let i = ref (-1) and a = ref Inf and b = ref true in
	for j = 0 to ((Array.length d) - 1) do
	(
		if e.(j) then
		(
			if !b then
			(
				b := false;
				a := d.(j);
				i := j;
			)
			else
			(
				if inferieur d.(j) (!a) then
				(
					a := d.(j)
					i := j;
				)
			)
		)
	)
	done; e.(!i) <- false; !i;;

*)

(* teacher: pouvait use poids type *)
let recherche_min d e =
	let res = ref (-1) in
	for i = 0 to ((Array.length d) - 1) do
		if e.(i) then
			if !res = (-1) || inferieur d.(i) d.(!res)
			then res := i
	done; if !res <> (-1) then e.(!res) <- false; !res;;

let relacher u d e w v =
	if e.(v) then (* "ne sert à rien" mais améliore  *)
		d.(v) <- mini d.(v) (som d.(u) w.(u).(v));;

(*

List.map renvoie liste
List.iter ne renvoie rien

*)

Array.make 1 3;;

let dijkstra g w s =
	let n = Array.length g in let d = Array.make n Inf and e = Array.make n true in
	for i = 0 to (n - 1) do
		d.(i) <- w.(s).(i)
	done;
	e.(s) <- false;
	(* ici fait un pour de 1 à n - 1 avec variable useless (permet d'éviter l'erreur de la boucle infini) ou while not (all false) *)
	for i = 0 to (n - 2) do (* pas 1 à n car on en a déjà géré un *)
		let u = recherche_min d e in
			List.iter (relacher u d e w) g.(u)
	done; d;;

(* chaque noeud strictement plus grand que son père (tous les étages remplis sauf le dernier eventuellement templi de la gauche vers la droite) *)

(*

Le tas est représenté par un vecteur t tel que:
t.(0) : taille du tas
racine en t.(1)
dernière feuille en t.(t.(0))
fils du sommet en position k sont en 2k, 2k + 1
le père // est en floor(k/2)

Ici les priorités sont les poids à l'extérieur du tas (dans d).
Donc on compare d.(t.(k)) et d.(t.(k / 2))

tas:
0 1 ... k
---------
n ..... i

d:
    i
---------
    k

indice:
    i
---------
    k

*)

tas = [|n; el0; ...; eln|];;
(*      0    1   2    n *)

let echange v i j =
	let t = v.(i) in
		v.(i) <- v.(j);
		v.(j) <- t;;

(* k est un indice pas un sommet *)
let rec monte d t indice k = match k with
| 1 -> ()
| k -> let j = k / 2 in if inferieur d.(t.(k)) d.(t.(j)) then
	(
		echange t k j;
		echange indice t.(k) t.(j);
		monte d t indice j;
	);;

let rec descend d t indice k = match k with
| k when 2*k > t.(0) -> ()
| k -> let j = if 2*k = t.(0) || inferieur d.(t.(2*k)) d.(t.(2*k+1))
then 2*k else 2*k+1 in
if inferieur d.(t.(j)) d.(t.(k)) then (echange t k j; echange indice t.(k) t.(j); descend d t indice j);;


(* pers:

let ajoute d t indice u =
	t.(0) <- t.(0) + 1; for
	t.(t.(0)) <- u;; *)

(* cf corrigé *)

(* pers: *)
let extrait d t indice =
	t.(0) <- t.(0) - 1;
	for i = 0 to Array.length indice do
		
	done

let relache_tas u d w tas indice v =


let dijkstra_tas g w s =

