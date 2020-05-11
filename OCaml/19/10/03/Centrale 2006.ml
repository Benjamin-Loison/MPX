(*

I.A.4) On supposera de plus que les caractères 0 à 9
sont représentés par des entiers consécutifs croissants

*)

let str = "test";;

print_int (String.length str);;

print_char str.[0];;

(*

How to ?

str.(0) <- 'M';;
String.set 0;; *)

(* one = *)
print_string (string_of_bool (str.[0] = 'c'));;

print_int (2 * 2);;

print_int (int_of_float (2. ** 4.));;

print_int (int_of_char 'c');;

let rec exprap x n = match n with
| 0 -> 1
| n -> let a = exprap x (n/2) in
	(if n mod 2 = 0 then 1 else x)*a*a;;

(* doesn't work but the idea is here *)
let decoder document =
	let index = ref 0 and count = ref 0
		and compting = ref false and fillStr = ref false and str = ref "" in
	for i = 0 to (String.length document) - 1 do
		if document.[i] == '[' then
			compting := true;
		if document.[i] == ']' then
			compting := false;
		if !fillStr then
			let chr = char_of_int document.[i];
			for i = 0 to !count do
				str := (!str)@chr;
			done;
			index := 0;
			count := 0;
			fillStr := false;
		if !compting && document.[i] != '[' then
			count := !count + (int_of_char document.[i]) * (exprap 10 !index);
			index := !index + 1;
	done;
	str;;

decoder "[2]a[2]b[2]c";;

(* personnal tests *)

7 / 2;;

let l = [1; 2; 3];;

let rec test l = match l with
| [] -> []
| t::q -> test q;;

test l;;

fst(1, 2);;