let rec len l = match l with
| t::q -> 1 + len q
| _ -> 0;;

let l0 = [1; 2; 4];;
len l0;;
List.length l0;;

let rec maxou l = match l with
| [] -> failwith "no element"
| [a] -> a
| [t;q] -> max t q
| a::b::c -> max (max a b) (maxou c);;

(* (* assume != [], what to do if nothing about in the subject ? *)
let rec maximum l b = match l with
| t::q when t > b -> maximum q t
| t::q -> maximum q b
| _ -> b;;

let maxou l = maximum l (List.hd l);;

let rec maxou l = match l with
| t::q -> max (t maxou l)
| _ -> ;;*)

maxou l0;;
(* equivalent ? *)

(* mieux vaut mauvaise complexity mais avoir fait qqch *)
let rec rev l = match l with
| t::q -> (rev q)@[t] (* complexity @: linear en la premiere liste so quadratic here: problem *)
| _ -> [];;

let rev l =
	let rec aux l acc = match l with
		| [] -> acc
		| t::q -> aux q (t::acc)
	in aux l [];;

rev l0;;
List.rev l0;;
rev [1,2,3];; (* return same because need to use ; *)

4 = 42;;

let rec mem x l = match l with
| t::q -> t = x || mem x q
| _ -> false;;

List.mem 5 l0;;
List.mem 4 l0;;
mem 5 l0;;
mem 4 l0;;

let rec del x l = match l with
| t::q -> let l1 = del x q in if t = x then l1 else t::l1
| _ -> [];;
(* equivalent ? *)

(* teacher *)
let rec del x l = match l with
| [] -> []
| t::q when t = x -> del x q
| t::q -> t::(del x q);;

del 4 l0;;
del 5 l0;;

let l1 = [5; 7; 8];;

let rec concat l1 l2 = match l1 with
| t::q -> t::(concat q l2)
| _ -> l2;;

concat l0 l0;;
concat l0 l1;;

let f x = x * x;;

let rec map f l = match l with
| t::q -> (f t)::(map f q)
| _ -> [];;

map f l0;;
List.map f l0;;

(* one element one time in list *)
(* could be done in linear ? *)
(* quadratic: n1 * n2 *)
let rec union l0 l1 = match l0 with
| t::q -> let unioned = union q l1 in if List.mem t l1 then unioned else t::unioned
| [] -> l1;;

(* teacher *)
let rec reunion s1 s2 = match s1 with
| [] -> s2
| t::q when List.mem t s2 -> reunion q s2
| t::q -> t::(reunion q s2);;

let l2 = [2; 4; 9];;

union l0 l0;;
union l0 l1;;
union l0 l2;;

(* quadratic *)
let rec inter l0 l1 = match l0 with
| t::q -> let intered = inter q l1 in if List.mem t l1 then t::intered else intered
| _ -> [];;

(* teacher *)
let rec inter s1 s2 = match s1 with
| [] -> []
| t::q when List.mem t s2 -> t::(inter q s2)
| _::q -> inter q s2;;


inter l0 l0;;
inter l0 l2;;

let rec differ s1 s2 = match s1 with
| [] -> []
| t::q when List.mem t s2 -> differ q s2
| t::q -> t::(differ q s2);;

(* quadratic *)
let rec privat l0 l1 = match l0 with
| t::q -> let privated = privat q l1 in if List.mem t l1 then privated else t::privated
| [] -> [];;

l0;;
l2;;
privat l0 l2;;

(* quadratic en incluant privat union inter etc *)
let symDiff l0 l1 = privat (union l0 l1) (inter l0 l1);; (* yep *)

symDiff l0 l1;;
symDiff l0 l2;;

let impaire x = (x mod 2) = 1;;

let dernier l f =
	let rec aux l acc = match l with
	| t::q -> if f t then aux q t else aux q acc
	| _ -> acc;
	in let res = aux l (List.hd l) in if f res then res else failwith "no";;

let dernier f l =
	let rec aux l acc = match l with
	| [] -> if acc = [] then failwith "pas del" else List.hd acc
	| t::q when f t -> aux q (t::acc)
	| _::q -> aux q acc
	in aux l [];;

l0;;
dernier l0 impaire;;
l2;;
dernier l2 impaire;;
let l3 = [2; 4; 8];;
dernier l3 impaire;;

not (1 = 2);;

(* let double l =
	let contains = ref [] in
		let rec aux l = match l with
		| t::q -> if (not (List.mem t contains)) then contains := t::(!contains) in aux q
		| _ -> ()
		in aux l in contains;; *)

let l4 = [5; 5; 6];;
del 5 l4;; (* delete all *)

let double l = 
	let rec aux l acc = match l with (* peut commencer par [] comme ça on a le fonctionnement *)
	| t::q when List.mem t q -> aux (del t q) (t::acc)
	| t::q -> aux (del t q) acc
	| _ -> acc
	in aux l [];;

(* same as before for complexity *)
let double l =
	let rec aux l acc = match l with
	| [] -> acc
	| t::q when (List.mem t q) && not (List.mem t acc) -> aux q (t::acc)
	| _::q -> aux q acc
	in aux l [];;

double l4;;
double l0;;

(* let double l =
	let rec aux l acc0 acc1 = match l with
		| [] -> acc1
		| t::q -> if List.mem t acc0 then aux q (del t acc0) acc1 else if (not (List.mem t acc1)) and not (List.mem t acc0)) then
	in aux l [];; *)

let rec pref l =
	let rec aux l acc = match l with
	| t::q -> aux q (pref t::acc)
	| _ -> acc
	in aux l [];;

pref l0;;
pref l2;;

type exp = Const of float | X | Somme of exp * exp | Produit of exp * exp | Puiss of exp * int;;

let a = Produit(Puiss(X, 2), Somme(X, Const 1.5));;

let rec str_of_exp e = match e with
| Const c -> string_of_float c
| X -> "x"
| Somme(e1, e2) -> "(" ^ (str_of_exp e1) ^ " + " ^ (str_of_exp e2) ^ ")"
| Produit(e1, e2) -> "(" ^ (str_of_exp e1) ^ " * " ^ (str_of_exp e2) ^ ")"
| Puiss(e1, e2) -> "(" ^ (str_of_exp e1) ^ " ** " ^ (string_of_int e2) ^ ")";;

let s = "MP *";;

s;;
s.[0];;

let substr s i j =
	let ns = ref "" in
	for k = i to j do
		ns := !ns ^ s.[k]
	done;
	!ns;;

(* let normalien s = *)

let string_of_exp e = let s = str_of_exp e in String.sub s 1 ((String.length s) - 2);;

string_of_exp a;;
str_of_exp a;;

let rec image e x = match e with
| Const c -> c
| X -> x
| Somme(e1, e2) -> (image e1 x) +. (image e2 x)
| Produit(e1, e2) -> (image e1 x) *. (image e2 x)
| Puiss(e, n) -> (image e x) ** (float_of_int n);;

image a 1.;;

let rec derive e = match e with
| Const c -> Const 0.
| X -> Const 1.
| Somme(e1, e2) -> Somme(derive e1, derive e2)
| Produit(e1, e2) -> Somme(Produit(derive e1, e2), Produit(e1, derive e2))
| Puiss(e1, e2) -> Produit(Produit(Const (float_of_int e2), Puiss(derive e1, e2 - 1)), e1);;

let d = derive a;;
string_of_exp d;;

(*

(((2. * (1. ** 1)) * x) * (x + 1.5)) + ((x ** 2) * (1. + 0.))
2x * (x + 1.5) + (x ** 2)
2x² + 3x + x²
3x² + 3x

*)

type zbarre = Moins_infini | Plus_infini | Valeur of int;;

7;;
-3;;

let p = [1; 0; -3; 5; -7];;

(* Assuming that p respect rules *)
let deg p = let d = List.length p in if d > 0 then Valeur (d - 1) else Moins_infini;;

(* Teacher *)
let degre p = match p with
| [] -> Moins_infini
| _ -> Valeur (List.length p - 1);;

let nul = [];;
let a = [1];;

deg p;;
deg nul;;
deg a;;

let id = [1; 0];;

(*let eval p n =
	let s = ref 0 in
	for i = 0 to (List.length p) - 1 do
		s := !s + p.
	done;
	s;;*)

2. ** 3.;;

7 / 2;;

let rec exprap x n =
	if x = 0 then 1
	else
		let a = exprap x (n / 2) in
			(if (n mod 2) = 1 then x else 1) * a * a;;

(* teacher *)
let rec exprap x n = match n with
| 0 -> 1
| n -> let c = exprap x (n / 2) in
	(if (n mod 2) = 1 then x else 1) * c * c;;

exprap 2 4;;

(*let eval p n =
	let rec aux p acc = match p with
	| t::q -> aux q (acc +. (t) * (int_of_float (float_of_int n) ** (float_of_int (List.length p))))
	| _ -> 0
	in aux p 0;;*)

let eval p n =
	let rec aux p acc = match p with
	| t::q -> aux q (acc + t * exprap n (List.length p))
	| _ -> 0
	in aux p 0;;

(* teacher *)
let eval p x =
	let rec aux l puiss = match l with
	| [] -> 0
	| t::q -> t * (exprap x puiss) + aux q (puiss - 1) in aux p (List.length p - 1);;

eval nul 0;;
eval nul 1;;
eval a 0;;
eval a 1;;
eval id 0;;
eval id 1;;

let horner p x =
	let rec aux p = match p with
	| [] -> 0
	| t::q -> t + x * (aux q) in aux (List.rev p);;

horner nul 0;;
horner nul 1;;
horner a 0;;
horner a 1;;
horner id 0;;
horner id 1;;