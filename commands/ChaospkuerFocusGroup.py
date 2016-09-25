import sublime, sublime_plugin

class ChaospkuerFocusGroup(sublime_plugin.WindowCommand):
	def run(self, **args):
		self.window.run_command("focus_group", {"group":args["group"]})
		sublime.set_timeout_async( lambda: self.window.focus_group(args["group"]) )
