with import <nixpkgs> {};

stdenv.mkDerivation {
	name = "env";
	buildInputs = [
		pkgs.python36
		pkgs.imagemagick
	];
}
