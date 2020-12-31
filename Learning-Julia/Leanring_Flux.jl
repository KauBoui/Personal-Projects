### A Pluto.jl notebook ###
# v0.12.17

using Markdown
using InteractiveUtils

# ╔═╡ 2a9f17c8-3e50-11eb-1618-7b3ad10e010c
begin
	using Flux
	using Flux : accuracy
	using MLDatasets
end

# ╔═╡ dd287908-3e52-11eb-1db1-25825d136ded
begin
	train_x, train_y = MNIST.traindata()
	test_x, test_y = MNIST.testdata()
end

# ╔═╡ 448c565e-3e54-11eb-1a75-3d7724143abe
begin
	m = @Chain(
		Input(784),
		Affine(128), relu,
		Affine(64), relu,
		Affine(10), softmax)
	model = mxnet(m)
end

# ╔═╡ Cell order:
# ╠═2a9f17c8-3e50-11eb-1618-7b3ad10e010c
# ╠═dd287908-3e52-11eb-1db1-25825d136ded
# ╠═448c565e-3e54-11eb-1a75-3d7724143abe
