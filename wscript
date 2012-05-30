srcdir = '.'
builddir = 'build'
VERSION = '0.0.1'

def set_options(opt):
    opt.tool_options('compiler_cxx')

def configure(conf):
    conf.check_tool('compiler_cxx');
    conf.check_tool('node_addon');
    conf.env['CXXFLAGS'] = ['-fPIC'];

def build(bld):
    obj = bld.new_task_gen('cxx', 'shlib', 'node_addon');
    obj.source = ['multimarkdown.cc'];
    obj.target = 'multimarkdown';
    obj.add_obj_file("deps/peg-multimarkdown/markdown_lib.o");
    obj.add_obj_file("deps/peg-multimarkdown/markdown_parser.o");
    obj.add_obj_file("deps/peg-multimarkdown/markdown_output.o"); 
    obj.add_obj_file("deps/peg-multimarkdown/GLibFacade.o"); 
