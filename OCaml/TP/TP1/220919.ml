let rec prefixe l = match l with
| [] -> []
| t::q -> [t]::(List.map (fun l -> t::l) (prefixe q));;

(* not so clear *)

let l = [0; 1; 2; 3];;

prefixe l;;

let p = [1; 0; -3; 5; -7];; (* X^4 - 3X^2 + 5X - 7 *)
let pn = [-1; 0; -3; 5; -7];; (* -X^4 - 3X^2 + 5X - 7 *)

let r = [1; -3; 5; -7];; (* X^3 - 3X^2 + 5X - 7 *)
let rn = [-1; -3; 5; -7];; (* -X^3 - 3X^2 + 5X - 7 *)

type zbarre = Moinsinfini | Plusinfini | Valeur of int ;;

let horner p x0 =
let rec aux p = match p with
| [] -> 0
| t :: q -> t + x0 *(aux q) in aux (List.rev p);;

(* TEACHER MISTAKE *)
let limite p x = match x,p with
| _ , [] -> Valeur 0
| _ , [a] -> Valeur a
| Moinsinfini, t :: q when t < 0 -> if List.length p mod 2 = 0 then Plusinfini else Moinsinfini (* 2 = 1 *)
| Moinsinfini, t::q -> if List.length p mod 2 = 0 then Moinsinfini else Plusinfini (* 2 = 1 *)
| Plusinfini, t :: q -> if t < 0 then Moinsinfini else Plusinfini
| Valeur a, _ -> Valeur (horner p a);;

limite p Moinsinfini;; (* +inf *)
limite pn Moinsinfini;; (* -inf *)
limite r Moinsinfini;; (* -inf *)
limite rn Moinsinfini;; (* +inf *)

limite p Plusinfini;; (* +inf *)
limite pn Plusinfini;; (* -inf *)
limite r Plusinfini;; (* +inf *)
limite rn Plusinfini;; (* -inf *)

limite p (Valeur 2);; (* 7 *)
limite pn (Valeur 2);; (* -25 *)
limite r (Valeur 2);; (* -1 *)
limite rn (Valeur 2);; (* -17 *)

(* perfect *)

let rec normalize l = match l with
| [] -> []
| 0 :: q -> normalize q
| _ -> l;;

let addition p1 p2 =
let rec aux p1 p2 = match p1, p2 with
| _,[] -> p1
| [], _ -> p2
| x1 :: q1 , x2 :: q2 -> (x1 + x2) :: (aux q1 q2) in
normalize (List.rev (aux (List.rev p1) (List.rev p2)));;

let scalaire p a = List.map (fun x -> x*a) p;;
let multX p = p@[0];;

let produit p1 p2 = (* a revoir *)
	let rec aux p2 = match p2 with
	| [] -> []
	| t2::q2 -> addition (scalaire p1 t2) (multX (aux q2))
	in aux (List.rev p2);;

produit p r;; (* works *)