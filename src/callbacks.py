##@package src.callbacks
#Callbacks for the gui
#@author Newell Jensen

import gtk, shutil, sys, gnomevfs

######################################################
# Callback Methods
######################################################


def cb_enable_multiplier(menuitem, mw):

    if menuitem.get_active():
        mw[1].set_text(str(mw[0]*mw[2].get_value()))                
        mw[-1].set_sensitive(True)
    else:
        mw[1].set_text(str(mw[0]))        
        mw[-1].set_sensitive(False)


def cb_multiplier_changed(menuitem, mw):
    mw[1].set_text(str(mw[0]*menuitem.get_value()))


def cb_enable_internal_io_update(menuitem, mw):
    if menuitem.get_active():
        mw.set_sensitive(True)
    else:
        mw.set_sensitive(False)
        

def cb_internal_io_update_changed(menuitem, mw):
    mw[1].set_text(str(1.0/mw[0]*int(menuitem.get_active_text())))



def cb_open_control_window(menuitem, mw):
    pass


def cb_open_profile_window(menuitem, mw):
    pass


def cb_open_qsk_window(menuitem, mw):
    pass


def cb_open_ram_window(menuitem, mw):
    pass


def cb_open_register_window(menuitem, mw):
    pass


def cb_open_debug_window(menuitem, mw):
    pass


def cb_pll_button_pushed(menuitem, mw, status_bar):
    #TODO put logic that will poll the PLL_LOCKED pin to determine if
    # it is unlocked or not
    # Also need a global callback polling function that polls the pin
    # to let us know what the status of the PLL_LOCKED pin is
    status_bar.push(mw, 'Locked')





def cb_multi_spin(menuitem, mw, sysclk):
    mw.set_text(str(sysclk*menuitem.get_value_as_int()))


def cb_io_internal_update(menuitem, mw):
    sysclk = 25 # Need to change once I get sysclk
    if menuitem.get_active():
        for item in mw:
            item.set_sensitive(True)
        mw[1].set_text(str(1.0/sysclk*int(mw[0].get_active_text())))
    else:
        mw[1].set_text('')                    
        for item in mw:
            item.set_sensitive(False)


def cb_pulse_width(menuitem, mw, sysclk):
    mw.set_text(str(1.0/sysclk*int(menuitem.get_active_text())))
        

def cb_ioupdate(menuitem, mw):
    pass


def cb_load(menuitem, mw):
    pass


def cb_ext_pwr_pin_toggled(menuitem, mw):
    pass


def cb_profile_window_notebook(ram_button, ram_notebook, profile_notebook, profile_vbox):
    if ram_button.get_active():
        profile_vbox.remove(profile_notebook)
        profile_vbox.pack_end(ram_notebook)
    else:
        profile_vbox.remove(ram_notebook)
        profile_vbox.pack_end(profile_notebook)


def cb_enable_RAM(menuitem, mw):
    pass


def cb_load_RAM(menuitem, mw):
    pass


def cb_load_RAM_file(menuitem, mw):

    def response_to_dialog(entry, dialog, response):
        dialog.response(response)

    load_RAM_dialog = gtk.MessageDialog(mw,
                                        (gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT),
                                        gtk.MESSAGE_INFO,
                                        gtk.BUTTONS_OK_CANCEL,
                                        gtk.STOCK_DIRECTORY)
    load_RAM_dialog.set_markup('<b>Please enter new folder name:</b>\nIf the folder name you choose exists\non disk in this directory it will deleted.')
    entry = gtk.Entry()
    entry.show()
    entry.connect('activate', response_to_dialog, load_RAM_dialog, gtk.RESPONSE_OK)
    hbox = gtk.HBox()
    hbox.show()
    hbox.pack_end(entry)
    load_RAM_dialog.vbox.pack_end(hbox, True, True, 0)
    load_RAM_dialog.show()
    response = load_RAM_dialog.run()
    text = entry.get_text()        
    if response == gtk.RESPONSE_OK and text.strip() != '':
        pass
    load_RAM_dialog.destroy()


def cb_new_file(menuitem, mw):
    """!
    Event handler for 'New File'.
    @param menuitem menuitem that threw the event
    @param mw current mw instance
    """
    pass


def cb_open_file(menuitem, mw):
    """!
    Event handler for 'Open File'.
    @param menuitem menuitem that threw the event
    @param mw current mw instance
    """
    pass


def cb_close_file(menuitem, mw):
    """!
    Event handler for 'Close File'.
    @param menuitem menuitem that threw the event
    @param mw Mw object
    @param mw current mw instance
    """
    pass


def cb_show_about_dialog(menuitem, mw):
    """!
    Event handler for About menu button.
    @param menuitem about menuitem that threw the event
    @param mw Mw object
    """
    mw.aboutdialog.show()
    mw.aboutdialog.run()
    mw.aboutdialog.hide()


def cb_destroy(event, mw):
    """!
    Event handlder when the form is closed in any fashion.
    @param event event that was thrown
    """
    gtk.main_quit()
