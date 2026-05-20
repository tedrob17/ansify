import ansify

print(f"{ansify.boldText("**Core Functions**")}")
ansify.banner("Hello world!")
ansify.success("Yes!")
ansify.warn("Uhh.")
ansify.error("That's not good..")
print(ansify.boldText("Ooh, bold!"))

print(f"\n{ansify.boldText("**Paint Engine**")}")

critical = ansify.paint(" Critical Error ", colour=ansify.white, bg=ansify.bg_red, is_bold=True)
print(critical)

underlined = ansify.paint("Read Online", is_underline=True, colour=ansify.cyan)
print(underlined)