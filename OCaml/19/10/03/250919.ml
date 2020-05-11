type arbre = Vide | N of int * arbre * arbre;;

(* ok *)
let rec countFeuilles a = match a with
| Vide -> 0
| N(_, Vide, Vide) -> 1
| N(_, g, d) -> countFeuilles g + countFeuilles d;;

let a = N(5, N(3, N(2, Vide, Vide), N(4, Vide, Vide)), N(7, Vide, N(8, Vide, Vide)));;

countFeuilles a;;

(* ok *)
let rec hauteur a = match a with
| Vide -> -1
| N(e, g, d) -> 1 + max (hauteur g) (hauteur d);;

hauteur a;;

(* ok *)
let rec taille a = match a with
| Vide -> 0
| N(e, g, d) -> 1 + (taille g) + (taille d);;

taille a;;

(* ok *)
let rec recherche a x = match a with
| Vide -> false
| N(e, g, d) -> x = e || recherche g x || recherche d x;;

recherche a 2;;
recherche a 5;;
recherche a 3;;
recherche a 42;;

let rec mirror a = match a with
| N(e, g, d) -> N(e, mirror d, mirror g)
| Vide -> Vide;;

mirror a;;

(* TODO: optimize then *)

(* TODO with accumulators *)
(* ok *)
let rec labels a p = match a with
| N(e, _, _) when p = 0 -> [e]
| N(e, g, d) -> (labels g (p - 1))@(labels d (p - 1))
| Vide -> [];;

(* teacher *)
let labels a p =
	let rec aux a ind acc = match a with
	| Vide -> acc
	| N(e, g, d) -> if ind = p then e::acc
						 else aux g (ind + 1) (aux d (ind + 1) acc)
	in aux a 0 [];; (* retourne les valeurs dans quel ordre ? *)

labels a 0;;
labels a 1;;
labels a 2;;
labels a 3;;

(* ok *)
let rec egal a b = match a, b with
| N(e, g, d), N(r, h, f) -> e = r && egal g h && egal d f
| Vide, Vide -> true
| Vide, _ | _, Vide -> false;;

egal a a;;

let b = N(5, N(3, N(2, Vide, Vide), N(4, Vide, Vide)), N(7, Vide, N(9, Vide, Vide)));;

egal a b;;

(* teacher *)
(* b sarbre de a *)
let rec sarbre a b = match a with
| Vide -> b = Vide
| N(xa, ga, da) -> egal a b || sarbre ga b || sarbre da b;;

(* incorrect *)
let sarbre a b =
	let rec aux a b = match a, b with
	| N(e, Vide, Vide), N(f, Vide, Vide) (* when e = f *) -> true
	| N(e, g, d), _ -> egal g b || egal d b
	| Vide, _ -> false
	in egal a b || aux a b;;

sarbre a a;;
sarbre b a;;
sarbre a b;;

let c = N(3, N(2, Vide, Vide), N(4, Vide, Vide));;
let d = N(4, Vide, Vide);;

sarbre a c;;
sarbre a d;;

(* teacher *)
(* don't work well said teacher *)
let testabr a =
	let rec aux a = match a with
	| Vide -> (true, max_int, min_int) (* /!\ pas inverse *)
	| N(e, Vide, Vide) -> (true, e, e)
	[ N(e, g, d) ->
		let (boolg, ming, maxg) = aux g and
			 (boold, mind, maxd) = aux d in
			 (boolg && boold && maxg < e && mind > e, ming, maxd) in
			 let (bool, _, _) = aux a in bool;;

(* incorrect *)
let rec abr a = match a with
| Vide -> true
| N(e, g, d) -> (match g with
					 | N(r, h, f) -> r < e
					 | Vide -> true) &&
					 (match d with
					 | N(r, h, f) -> r > e
					 | Vide -> true) && abr g && abr d;;

abr a;;
abr b;;

let e = N(5, N(3, N(3, Vide, Vide), N(4, Vide, Vide)), N(7, Vide, N(8, Vide, Vide)));;

abr e;;

(* ok /!\ unicitié label *)
let rec insere a x = match a with
| Vide -> N(x, Vide, Vide)
| N(e, g, d) when x = e -> a
| N(e, g, d) -> if y < x then N(e, insere g x, d) else N(e, g, insere d x);;

insere Vide 4;;
insere a 9;; (* fine *)

let arbre_of_list l =
	let rec cAbr a l = match l with
	| [] -> a
	| t::q -> cAbr (insere a t) q
	in cAbr Vide l;;

let l = [1; 2; 3; 4];;

arbre_of_list l;; (* peigne *)
arbre_of_list [42; 45; 14; 26; 31];;

arbre_of_list (List.rev l);;

Random.self_init();;
Random.int 2;; (* up excluded *)

let randomFrom l =
	Random.self_init() in;; (* nope, could be nice if tableau and not list *)

(* insert root: ENLEVER X *)
(* teacher *)
let rec decoupe a x = match a with (* signature de la fonction *)
| Vide -> Vide, Vide
| N(e, g, d) when e = x -> g, d
| N(e, g, d) when e > x ->
	let gr, dr = decoupe g x in gr, N(e, dr, d)
| N(e, g, d) -> let gr, dr = decoupe d x in N(e, g, gr), dr;;

let inser_rac x a = match a with
| Vide -> N(x, Vide, Vide)
| N(e, g, d) -> let (b, c)

(* syntax error: let rec f = 2;; *)

(* not peigne search *)
(* don't use abr properties here *)
(* INCORRECT *)
let maxAbr a =
	let rec aux a maxi = match a with
	| N(e, g, d) -> max e (max (aux g maxi) (aux d maxi))
	| Vide -> maxi
	in aux a min_int;;

let maxAbr a =
	let rec aux a maxi = match a with
	| N(e, _, d) -> aux d e
	| Vide -> maxi
	in if a = Vide then failwith "Empty" else aux a min_int;;

min_int;;

a;;
maxAbr a;;
b;;
maxAbr b;;
c;;
maxAbr c;;
d;;
maxAbr d;;

(* could test if n not > max *)
let rec supAbr a n = match a, n with
| Vide -> 
| N(e, g, d) -> if (maxAbr g) < n;;

let rec fusion a b = match a, b with
| N(c, d, e), N(f, g, h) -> let i = maxAbr 
|;;

let delMaxAbr a =
	let maxi = maxAbr a in
		let rec aux a = match a with
		| N(e, Vide, Vide) when e = maxi -> Vide
		| N(e, g, d) -> N(e, g, aux d)
		| Vide -> Vide
	in aux a;;

a;;

delMaxAbr a;;

(* teacher *)
let success a x =
	let rec etiqmin a = match a with
	| Vide -> failwith "Vide"
	| N(e, Vide, _) -> e
	| N(_, g, _) ->
		etiqmin g in let _, d = decoupe a x in etiqmin d;;

(* supprimer 1 élément revient à supprimer la racine d'un arbre *)

let rec supprMax a = match a with
| Vide -> failwith "Vide"
| N(x, g, Vide) -> x, g
| N(x, g, d)-> let maxd, dr = supprMax d in maxd, N(x, g, dr);;

let rec supprime x a = match a with
| Vide -> Vide
| N(e, g, d) ->
	if x < e then
		N(e, supprime x g, d)
	else
		if x > e then
			N(e, g, supprime x d)
		else
			if g = Vide then d
			else let maxg, gr = supprMax g in N(maxg, gr, d);;

(* pas arbre aux DS samedi *)

