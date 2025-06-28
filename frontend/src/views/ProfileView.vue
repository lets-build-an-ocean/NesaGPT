<template>
	<div class="container w-screen text-center">
		<img
			class="rounded-full h-50 w-50 object-cover p-1 mx-auto mb-4 hover:bg-gray-400"
			:src="store.picture"
			alt=""
		/>
		<div class="w-[50%] mx-auto text-left">
			<p class="p-3">
				Email :
				<input
					class="border-1 border-gray-300 rounded-md p-1"
					type="text"
					:value="store.email"
				/>
			</p>
			<div>
				<p class="p-3">
					Name :
					<input
						class="border-1 border-gray-300 rounded-md p-1"
						type="text"
						:value="store.username"
					/>
				</p>
			</div>
			<p class="">
				Balance : {{ store.balance }}

				<button
					class="mx-auto mt-5 border-1 border-green-600 bg-green-600 rounded-2xl hover:bg-green-800 hover:text-white p-2"
					@click=""
				>
					شارژ حساب کاربری
				</button>
			</p>
		</div>
	</div>
</template>
<script setup>
	import { store } from "../store.js";
</script>
