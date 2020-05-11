type g_l = {mutable n:int; mutable voisins : int list array};; (* peut changer taille tableau grâce à mutable *)

let g_ex = {n=6; voisins=[|[1; 4]; [4; 5]; [1; 3]; [4]; []; [2]|]};;

(* ou *)
let ex1 = Array.make 6 [];;
ex1.(0) <- [1; 4];;
(* ... *)

let g_ex = {n=6; voisins=ex1};;

(* Array.find [] g_ex;; *)
List.mem [] 1;;

let rec addListeTriee l e = match l with
	| [] -> [e]
	| t::q when t < e -> t::(addListeTriee q e)
	| t::q when t = e -> l
	| t::q -> e::l;;

(* example first: add 0 1 *)
let ajoute_arete g i j =
	g.voisins.(i) <- addListeTriee g.voisins.(i) j;;

let rec delList l e = match l with
| [] -> []
| t::q when t < e -> t::(delList q e)
| t::q when t = e -> q
| t::q -> l;;

let supp_arete g i j =
	g.voisins.(i) <- delList g.voisins.(i) j;;

let ajoute_sommet g =
	let v = Array.make g.n [] in
		for i = 0 to g.n do
			v.(i) <- g.voisins.(i)
		done;
	g.n <- g.n + 1;
	g.voisins <- v;;

(* or *)
let ajoute_sommet g =
	g.n <- g.n + 1;
	g.voisins <- Array.append g.voisins [|[]|];;

let a = [|0; 1; 2|];;
(* Array.append renvoie le vecteur *)
Array.append a a;;

let rec patchList l e = match l with
| [] -> []
| t::q when e < t -> (t - 1)::(patchList q e)
| t::q when e = t -> patchList q e
| t::q -> t::(patchList q e);;

let supprime_sommet g i =
	g.n <- g.n - 1;
	let v = Array.make g.n [] in
		for j = 0 to (i - 1) do
			v.(j) <- patchList g.voisins.(j) i
		done;
		for j = i to (g.n - 1) do
			v.(i) <- patchList g.voisins.(j + 1) i
		done;
		g.voisins <- v;;

(* le graphe n'est pas mutable mais ses champs oui *)

(* let rec desoriente g i j = match g.voisins.(i) with
| [] -> ()
| t::q -> ajoute_arete g t j;;

let add l0 l1 = match l0 with
| [] -> []
| t::q -> 

let desoriente g =
	for i = 0 to g.n do
		g.voisins.(i) <- desoriente g 0  
	done;; *)

let desoriente g =
	let rec aux l i = match l with (* parcourir voisins d ei et pour chaque voisin rajoute j i *)
	| [] -> ()
	| t::q -> ajoute_arete g t i; aux q i
	in for i = 0 to g.n - 1 do
		aux g.voisins.(i) i done;;

(* graphe simple: aucun sommet n'est relié à lui-même *)

