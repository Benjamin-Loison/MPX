type arete = {a: int; b: int};;
type graphe = {n: int; aMaj: arete list};;

let gex1 = {n = 5; aMaj = [{a=0; b=4}; {a=4; b=3}; {a=0; b=3};
			               {a=1; b=3}; {a=0; b=3}; {a=3; b=0}]};;

let rec insere l e = match l with
| [] -> [e]
| t::q when e > t -> t::(insere q e)
| t::q when e <> t -> e::l
| t::q -> l;;

insere [] 2;;

insere [3] 2;;
insere [3] 4;;
insere [1; 4; 6; 7; 9] 8;;

(* linéaire *)

let voisins g s =
	let l = ref [] in
	let rec aux aMaj = match aMaj with
	| [] -> ()
	| t::q -> if t.a = s then l := insere !l t.b
			 else if t.b = s then l := insere !l t.a;
			 aux q;
	(*for i = 0 to g.n do
		let ar = g.aMaj.(i) in
		if ar.a = s then (* a et b distincts *)
			insere l ar.b
		else if ar.b = s then
			insere l ar.a
	done;*)
	in aux g.aMaj;
	!l;;

for i = 0 to 4 do
	voisins gex1 i (* can't be used even following lines work... *)
done;;

voisins gex1 0;;
voisins gex1 1;;
voisins gex1 2;;
voisins gex1 3;;
voisins gex1 4;;

1 = 2;;

let gex2 = {n = 6; aMaj = [{a=0; b=3}; {a=0;b=5}; {a=1;b=2}; {a=1;b=4};
									{a=3;b=4}; {a=2;b=5}]};;

(* 4.

 1 2 3
 
 1 2 3
 

 2 2 2
 
 1 1 1

gex1:

1 2
    1
3 1

*)

Array.make 2 4;;

let coloration g =
	let t = Array.make g.n 0 in
	for i = 0 to (g.n - 1) do
		let v = voisins g i in
			 let rec aux v b = match v with
			 | [] -> b
			 | a::q when t.(a) = 0 -> b
			 | a::q when t.(a) < b -> aux q b
			 | a::q -> aux q (t.(a) + 1) (* proof ? *)
			 in t.(i) <- aux v 1;
	done;
	t;;

voisins gex2 0;;
voisins gex2 2;;

coloration gex1;;
coloration gex2;;

(*

6.

existence: il existe forcément nbc(G), tel que fc(G, nbc(G)) != 0, exemple:
	n(G) donc il existe un rang tel que != 0 et à partir de ce rang fc(G, p)
	est != 0 car cela revient par récurrence à ne pas utiliser la nouvelle couleure

unicité: par l'absurde supposons l'existence de nbc(G) et nbc'(G)
	distincts, on a alors clairement min(nbc(G), nbc'(G)) qui
	n'appartient pas à EC(G): contradiction

*)

(* 7. si aucune arrête tous les sommets peuvent avoir la même coloration
	donc nbc(G) = 1
	
	ayant le choix du nombre pour la coloration pour chaque sommet
	parmis [| 1; n |], on a donc fc(G,p)=p^(n(G))
*)

(* 8.

tous les sommets sont reliés à tous les autres:
on a donc nbc(G) = n(G) et fc(G, p) TODO

*)

(* 9. 3 ok, 2 clrmnt imp
*)

let prem_voisin g s =
	List.hd (voisins g s);;

let prem_ni g =
	let i = ref 0 and b = ref 0 in
	while !i < (g.n - 1) do
		if (List.length (voisins g !i)) <> 0 then (b := !i; i := g.n);
		incr i
	done;
	!b;;

prem_ni gex1;;
prem_ni gex2;;

let h g =
	let s1 = prem_ni g in
	let s2 = prem_voisin g s1 in
	let rec aux l = match l with
	| [] -> []
	| t::q when (t.a = s1 && t.b = s2) || (t.b = s1 && t.a = s2) -> aux q
	| t::q -> t::(aux q)
	in {n = g.n; aMaj = aux g.aMaj};;

h gex1;;
h gex2;;

let k g =
	let s1 = prem_ni g in
	let s2 = prem_voisin g s1 and hg = h g in
	let chg i = if i = s2 then s1 else (if i > s2 then i - 1 else i) in
	let rec aux l = match l with
	| [] -> []
	| t::q -> {a = chg t.a; b = chg t.b}::(aux q)
	in {n = g.n - 1; aMaj = aux hg.aMaj};;

gex1;;
h gex1;;
k gex1;;

gex2;;
h gex2;;

let s1 = prem_ni gex2;;
prem_voisin gex2 s1;;

k gex2;; (* checked *)

(*


14.



*)

let testArray a =
	a.(0) <- 0;;

let b = [|1; 2|];;
testArray b;;
b;;

let testList a = a@[0];;
let c = [1; 2];;
testList c;;
c;;

let difference p q = (* TO KNOW: does array or list are like pointers in argument - only array are mutable (sure ?) *)
	let r = Array.copy p in
	for i = 0 to (Array.length q) - 1 do
		r.(i) <- r.(i) - q.(i)
	done;
	r;;

let p = [|1; 2; 3|];;
let q = [|4; 5; 6|];;
difference p q;;

let Pc g =
	;;

let eval p x =
	let n = Array.length p in
	let res = ref p.(n - 1) in
	for i = 2 to n do
		res := x * (!res) + p.(n - i)
	done;
	!res;;

eval p 0;;
eval p 1;;

let nbc g =
	;;


